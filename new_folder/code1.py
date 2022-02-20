import math

def find_max_distance(arr):
	
	# Write your code here
	av=int(avg(arr))
	firstnotfound=True
	first,last=-1,-1
	for i in range(len(arr)):	
		if arr[i]==av and firstnotfound:
			first=i
			firstnotfound=False
        
		elif arr[i]==av:
			last=i
	if last==-1:
		return -1
	return last-first

N = input()
arr = list(map(int, input().split()))
print(find_max_distance(arr))