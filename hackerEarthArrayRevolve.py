# Array revolve
# Max. Marks: 100
# You are given an array A(1-based index) consisting of N integers. You have to process two types of queries on this array.

# Type 1: Given ID and VAL, perform the operation UPDATE(ID, VAL)
#     UPDATE(ID, VAL):
#         if VAL == 0:
#             return
#         AID = AID + VAL
#         if ID == N:
#             UPDATE(1, VAL - 1)
#         else :
#             UPDATE(ID + 1, VAL - 1)

# Type 2: Given L and R, find QUERY(L, R)
#     QUERY(L, R):
#         if L == R:
#             return AL
#         if L == N:
#             return AL + QUERY(1, R) 
#         else :
#             return AL + QUERY(L + 1, R)
# Input:

# The first line of input contains two space separated integer N and Q denoting size of array and number of queries respectively.
# The second line contains N space separated integers denoting array A.
# Next Q lines are of one of the following format:
# 1 ID VAL : for type 1 query
# 2 L R : for type 2 query
# Output:

# For each type 2 query, output the answer modulo 109+7 in a new line.
# Constraints:

# SAMPLE INPUT 
# 6 5
# 4 1 2 3 9 1
# 2 2 5
# 1 4 5
# 2 6 6
# 1 2 4
# 2 3 1
# SAMPLE OUTPUT 
# 15
# 4
# 39
# Explanation
# Initial Array A[] = {4, 1, 2, 3, 9, 1}

# 1st query: 1 + 2 + 3 + 9 = 15

# 2nd query: Updated Array A[] = {6, 2, 2, 8, 13, 4} 

# 3rd query: 4

# 4th query: Updated Array A[] = {6, 6, 5, 10, 14, 4}

# 5th query: 5 + 10 + 14 + 4 + 6 = 39



def query1(N,Arr,ID,Val):
    #Write your code here
    ID-=1
    while(Val>0):
        Arr[ID]+= Val
        Val-=1
        ID= (ID+1)%N
        
    

def query2(N,Arr,L,R):
    L-=1
    R-=1
    if L==R:
        return Arr[L]
    if L<R:
        sum1=0
        for i in range(L,R+1):
            sum1+=Arr[i]
        return sum1%(10**9+7)
    else:
        sum1=0
        for i in range(R+1):
            sum1+=Arr[i]
        for i in range(L,N):
            sum1+=Arr[i]
        return sum1%(10**9+7)
            
    
N,Q = map(int,input().split())
Arr = list(map(int,input().split()))
for _ in range(Q):
    type,X,Y = map(int,input().split())
    if type==1:
        query1(N,Arr,X,Y)
    else:
        print (query2(N,Arr,X,Y))