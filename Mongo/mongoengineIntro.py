from mongoengine import*

connect("db_mongoengine",host="mongodb://adwait:adwait22@adwaitscluster-shard-00-00-mueoy.mongodb.net:27017,adwaitscluster-shard-00-01-mueoy.mongodb.net:27017,adwaitscluster-shard-00-02-mueoy.mongodb.net:27017/test?ssl=true&replicaSet=AdwaitsCluster-shard-0&authSource=admin&retryWrites=true")

class User(Document):
    name = StringField()

class Page(Document):
    content = StringField()
    authors = ListField(ReferenceField(User))
    #referencefield says that the value of authors should be a user and ListField(ReferenceField(user)) means that it should be a list of users

bob = User(name="Bob Jones").save()
john = User(name="John Smith").save()

Page(content="Test Page", authors=[bob, john]).save()
Page(content="Another Page", authors=[john]).save()

# Find all pages Bob authored
Page.objects(authors__in=[bob])

# Find all pages that both Bob and John have authored
Page.objects(authors__all=[bob, john])

# Remove Bob from the authors for a page.
Page.objects(id='...').update_one(pull__authors=bob)

# Add John to the authors for a page.
Page.objects(id='...').update_one(push__authors=john)


