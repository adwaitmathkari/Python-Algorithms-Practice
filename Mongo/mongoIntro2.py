from pymongo import MongoClient

client = MongoClient('localhost:27017')

db = client.EmployeeData

#db.Employees.insert_one(
#        {
#        "id": employeeId,
#            "name":employeeName,
#        "age":employeeAge,
#        "country":employeeCountry
#        })
        
        
# Function to insert data into mongo db
def insert():
	try:
		employeeId = input("Enter Employee id")
		employeeName = input("enter name")
		db.Employees.insert_one({"id":employeeId, "name":employeeName})
		print('inserted 1 employee')
	except Exception(e):
		print(str(e))
		
		
#####
#####for i in range(20):
#####	print(i, 'times loop run')
#####	insert()

def read():
	try:
		empcol=db.Employees.find()
		print('\n all data from employeeData database \n')
		for emp in empcol:
			print(emp)
	except Exception(e):
		print(str(e))
		
		
#read()

def update():
	try:
		employeeId=input("enter id of the employee to modify")
		name=input("enter the change")
		db.Employees.update_one({"id": employeeId },{"$set": {"name":name,}})
		
		print('updated the info for one player having id:',employeeId )
		
	except Exception(e):
		print(str(e))
#
#update()
#read()
#update()
#read()
	
def delete():
	try:
		todel=input('enter id to delete')
		db.Employees.delete_many({"id":todel})
		print('deleted')
	except Exception(e):
		print(str(e))
		
		
#insert()
#delete()
#read()
#delete()
#read()
newCursor=db.Employees.find({"id":"1"})

for x in newCursor:
	print(x)
x1=db.getCollectionInfos
print(x1)
	
print(db.collection_names(include_system_collections=False))
#['Employees']

	
	
	
	
	