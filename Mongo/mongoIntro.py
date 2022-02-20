from pymongo import MongoClient
from pprint import pprint
#import pymongo
client = MongoClient("mongodb://adwait:adwait22@adwaitscluster-shard-00-00-mueoy.mongodb.net:27017,adwaitscluster-shard-00-01-mueoy.mongodb.net:27017,adwaitscluster-shard-00-02-mueoy.mongodb.net:27017/test?ssl=true&replicaSet=AdwaitsCluster-shard-0&authSource=admin&retryWrites=true")
db = client.testDatabase

# Paste the following examples here
#mongodb+srv://adwait:adwait22@adwaitscluster-mueoy.mongodb.net/test?retryWrites=true
print('client running')

db.inventory.insert_many([
   # MongoDB adds the _id field with an ObjectId if _id is not present
   { "item": "journal", "qty": 25, "status": "A",
       "size": { "h": 14, "w": 21, "uom": "cm" }, "tags": [ "blank", "red" ] },
   { "item": "notebook", "qty": 50, "status": "A",
       "size": { "h": 8.5, "w": 11, "uom": "in" }, "tags": [ "red", "blank" ] },
   { "item": "paper", "qty": 100, "status": "D",
       "size": { "h": 8.5, "w": 11, "uom": "in" }, "tags": [ "red", "blank", "plain" ] },
   { "item": "planner", "qty": 75, "status": "D",
       "size": { "h": 22.85, "w": 30, "uom": "cm" }, "tags": [ "blank", "red" ] },
   { "item": "postcard", "qty": 45, "status": "A",
       "size": { "h": 10, "w": 15.25, "uom": "cm" }, "tags": [ "blue" ] }
       ])


Student= {'id':1,
          'name':'xyz',
          'roll_no':1,
          'school_name':'abc',
          'school_address':
              {
                  'pin':123,
                  'area':'x',
                  'city':'y'
              },
          'address':
              {
                  'house_no':123,
                  'area':'abc',
                  'pin':123,
                  'city':'abc'
              },
          'standard':'c_101',
          'division':'abc'
          }
# class Student():
#     Student(id,name,roolno,schoolname,schooladdress,standard,division)
Standard={'standard_id': 'c_101','class_teacher': 'T_101','classroom_no':123}

Teacher={'teacher_id': 'T_101','teacher_name':'alan','education':'BE','specialization':'Mech','subjects':["maths","English"]}

studentColl=db.studentCollection
teacherColl=db.teacherCollection
standards=db.standards
studentColl.insert_one(Student)
teacherColl.insert_one(Teacher)
standards.insert_one(Standard)
print(db.collection_names())
# pprint.pprint(teacherColl.find_one())

for docu in teacherColl.find({}):
    pass
  #  #pprint(docu)

for docu in studentColl.find({}):
    pass
   # pprint(docu)

for doc in teacherColl.find({"teacher_name": "alan"}):
    pprint(doc)

print('done')