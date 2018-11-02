import json
import requests

#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#todos = json.loads(response.text)

response=requests.get("https://jsonplaceholder.typicode.com/todos")

todos=json.loads(response.text)

count=0
tasks={}
for todo in todos:
	if todo["completed"]:
		try:
			tasks[todo["userId"]]+=1
		except KeyError:
			tasks[todo["userId"]]=1
		
print(tasks.items())
topUsers = sorted(tasks.items(),key=lambda x: x[1], reverse=True)
max_complete = topUsers[0][1]

users = []
for user, num_complete in topUsers:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

print('top user is users are', max_users)

# Define a function to filter out completed TODOs 
# of users with max completed TODOS.
#def keep(variable):
#    is_complete = variable["completed"]
#    has_max_count = str(variable["userId"]) in users
#    return is_complete and has_max_count
#
## Write filtered TODOs to file.
#with open("filtered_data_file.json", "w") as data_file:
#    filtered_todos = list(filter(keep, todos))
#    json.dump(filtered_todos, data_file, indent=2)
#    
    
    

    
    
     