"""
#find the n-x th node
n=10
x=3

current = head



#nodes are [1,2,3,4,5,6,7,8,9,10]

#xlast is the pointer which will directly point to the answer when we reach the end 
xlast = head

count = 0

while current is not lastNode:
	
	current = current.next
	if count<x:
		count += 1
	else:
		xlast = xlast.next


iter 	current	 	xlast	 count 
1		1			1			0
2		2			1			1
3		3			1			2
4		4			1			3
5		5			2			3
6		6			3			3
7		7			4			3
8		8			5			3
9		9			6			3
10		10			7			3

terminate

1,2,3,4,5,6,7,8,9,10

"""

"""
def findXLast(head,x):
	
	count = 0
	current = head
	xlast = head
	
	while current.next:
		
		current = current.next
		
		if count < x:
			count+=1
		else:
			xlast = xlast.next
		
	return xlast



"""



#fibonachi


def fibonachi(x):	
	global d 
	if x==0:
		return 0
	if x==1:
		return 1
	
	if x in d.keys():
		return d[x]
	else:
		fib = fibonachi(x-1)+fibonachi(x-2)
		d[x]=fib
		return fib
d={}

print(fibonachi(4))



"""
		
employee system

create employee:
	https://api.emloyeemanagement.com/create/
	post request
	the request data will have emp details like name, address, gender etc
	
	create request to the database 
	
	send response 
	
		
"""

 