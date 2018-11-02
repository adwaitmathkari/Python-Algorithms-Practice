
from mongoengine import *
from datetime import datetime


connect('booksDb')


class BlogPost(Document):
    title = StringField()
    published_date = DateTimeField()

    meta = {
        'ordering': ['-published_date']
    }

def testBlogPost():
    blog_post_1 = BlogPost(title="Blog Post #1")
    blog_post_1.published_date = datetime(2010, 1, 5, 0, 0, 0)

    blog_post_2 = BlogPost(title="Blog Post #2")
    blog_post_2.published_date = datetime(2010, 1, 6, 0, 0, 0)

    blog_post_3 = BlogPost(title="Blog Post #3")
    blog_post_3.published_date = datetime(2010, 1, 7, 0, 0, 0)

    blog_post_1.save()
    blog_post_2.save()
    blog_post_3.save()

    # get the "first" BlogPost using default ordering
    # from BlogPost.meta.ordering
    latest_post = BlogPost.objects.first()
    assert latest_post.title == "Blog Post #3"

    # override default ordering, order BlogPosts by "published_date"
    first_post = BlogPost.objects.order_by("+published_date").first()
    assert first_post.title == "Blog Post #1"

# testBlogPost()

class Essay(Document):
    status = StringField(choices=('Published', 'Draft'), required=True)
    pub_date = DateTimeField()

    def clean(self):
        """Ensures that only published essays have a `pub_date` and
        automatically sets the pub_date if published and not set"""
        if self.status == 'Draft' and self.pub_date is not None:
            msg = 'Draft entries should not have a publication date.'
            raise ValidationError(msg)
        # Set the pub_date for published items if not set.
        if self.status == 'Published' and self.pub_date is None:
            self.pub_date = datetime.now()




#primarykey/id
#
# >>> class User(Document):
# ...     email = StringField(primary_key=True)
# ...     name = StringField()
# ...
# >>> bob = User(email='bob@example.com', name='Bob')
# >>> bob.save()
# >>> bob.id == bob.email == 'bob@example.com'
# True
class User(Document):
    country=StringField(required=True)
    name=StringField(primary_key=True,required=True)


class Page(Document):
    name=StringField()
    author=ReferenceField("User")
    published=BooleanField()


def addUsersandPages():
    u1 = User(name='sam', country='uk')
    u2 = User(name='bill', country='us')
    u3 = User(name='mohan', country='india')
    u4 = User(name='john', country='uk')
    p1 = Page(name='p1', author=u1, published=True)
    p2 = Page(name='p2', author=u2, published=False)
    p3 = Page(name='p3', author=u3, published=True)
    p4 = Page(name='p4', author=u3, published=True)
    p5 = Page(name='p5', author=u4, published=True)
    p6 = Page(name='p6', author=u4, published=True)


    for x in [u1, u2, u3, u4, p1, p2, p3, p4, p5, p6]:
        x.save()


def testquery1():
    addUsersandPages()
    # print(Page.objects)
    uk_users = User.objects(country='uk')
    uk_pages = Page.objects(author='john')
    testQ={}
    for page in uk_pages:
        print(page.name, page.author.name)

testquery1()

def querying():
    for user in User.objects:
        print(user.name)
    # This will return a QuerySet that will only iterate over users whose
    # 'country' field is set to 'uk'
    uk_users = User.objects(country='uk')

    uk_pages=Page.objects(author__country='uk')

    # Only find users whose age is 18 or less
    young_users = Users.objects(age__lte=18)
    #use __ne or __lte or __in
    # ne – not equal to
    # lt – less than
    # lte – less than or equal to
    # gt – greater than
    # gte – greater than or equal to
    # not – negate a standard check, may be used before other operators (e.g. Q(age__not__mod=5))
    # in – value is in list (a list of values should be provided)
    # nin – value is not in list (a list of values should be provided)
    # mod – value % x == y, where x and y are two provided values
    # all – every item in list of values provided is in array
    # size – the size of the array is
    # exists – value for field exists

    # string queries
    # exact – string field exactly matches value
    # iexact – string field exactly matches value (case insensitive)
    # contains – string field contains value
    # icontains – string field contains value (case insensitive)
    # startswith – string field starts with value
    # istartswith – string field starts with value (case insensitive)
    # endswith – string field ends with value
    # iendswith – string field ends with value (case insensitive)
    # match – performs an $elemMatch so you can match an entire document within an array

    #raw query (as done in pymongo)
    codingTag=Page.objects(__raw__={'tags': 'coding'})

    print (uk_users,uk_pages,codingTag,young_users)

    # Only the first 5 people
    users = User.objects[:5]

    # All except for the first 5 people
    users = User.objects[5:]

    # 5 users, starting from the 11th user found
    users = User.objects[10:15]



def queryAndFilter():

    """
    doc_cls is for Document class and the queryset is the one tho be filtered
    must be decorated by @queryset_manager
    """
    class BlogPost(Document):
        title = StringField()
        date = DateTimeField()

        @queryset_manager
        def date_sorted_objects(doc_cls, queryset):
            # This may actually also be done by defining a default ordering for
            # the document, but this illustrates the use of manager methods
            return queryset.order_by('-date')



    class BlogPost(Document):
        title = StringField()
        published = BooleanField()

        @queryset_manager
        def live_posts(doc_cls, queryset):
            return queryset.filter(published=True)

    BlogPost(title='test1', published=False).save()
    BlogPost(title='test2', published=True).save()
    assert len(BlogPost.objects) == 2
    assert len(BlogPost.live_posts()) == 1



    class AwesomerQuerySet(QuerySet):

        def get_awesome(self):
            return self.filter(awesome=True)

    class Page(Document):
        meta = {'queryset_class': AwesomerQuerySet}

    # To call:
    Page.objects.get_awesome()


    #Aggregation
    m_users = User.objects.count()
    yearly_expense = Employee.objects.sum('salary')
    mean_age = User.objects.average('age')

def advancedQueries():
    from mongoengine.queryset.visitor import Q

    # Get published posts
    Post.objects(Q(published=True) | Q(publish_date__lte=datetime.now()))

    # Get top posts
    Post.objects((Q(featured=True) & Q(hits__gte=1000)) | Q(hits__gte=5000))



    #Atomic queries
    post = BlogPost(title='Test', page_views=0, tags=['database'])
    post.save()
    BlogPost.objects(id=post.id).update_one(inc__page_views=1)
    post.reload()  # the document has been changed, so we need to reload it
    print(post.page_views)
    #1

    BlogPost.objects(id=post.id).update_one(set__title='Example Post')
    post.reload()
    print(post.title)
    #'Example Post'

    BlogPost.objects(id=post.id).update_one(push__tags='nosql')
    post.reload()
    print(post.tags)
    #['database', 'nosql']




    #
    # set – set a particular value
    # unset – delete a particular value (since MongoDB v1.3)
    # inc – increment a value by a given amount
    # dec – decrement a value by a given amount
    # push – append a value to a list
    # push_all – append several values to a list
    # pop – remove the first or last element of a list depending on the value
    # pull – remove a value from a list
    # pull_all – remove several values from a list
    # add_to_set – add value to a list only if its not in the list already




#
# http://docs.mongoengine.org/guide/querying.html
# https://www.mongodb.com/blog/post/building-your-first-application-mongodb-creating-rest-api-using-mean-stack-part-1