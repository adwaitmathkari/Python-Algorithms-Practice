#he
"""
4 rows 3 obstacles

- - - 
- 0 0 
- - - 
0 - - 




-0-
0--
-0-
-0-
-00
-0-
-00
00-
---
---
---

tc2


1
11 11
1 2
2 1
3 2 
4 2
5 2 
5 3 
6 2 
7 2
7 3
8 1
8 2



testcase 1..
2
4 3
2 2
2 3
4 1
2 3
2 1
2 2
2 3

output expected
4
1


"""


t = int(input())

for __ in range(t):
        
    n,q = map(int,input().split())
    
    l=[]
    for i in range(n):
        l.append([1,1,1])
        
    for _ in range(q):
        a,b = map(int, input().split())
        l[a-1][b-1] = 0
    
    acc = [1,1,1]
    fl = True
    
    # for l1 in l:
    #     print(l1)
    
    for row in range(n):
        newacc = [0,0,0]
        # col 0
        if l[row][0]==1 and (acc[0]==1 or acc[1]==1):
            newacc[0] = 1
        # col 1
        if l[row][1]==1 and (acc[0]==1 or acc[1]==1 or acc[2]==1):
            newacc[1] = 1
        # col 2
        if l[row][2]==1 and (acc[1]==1 or acc[2]==1):
            newacc[2] = 1
            
        acc = newacc[:]
        # print(row, newacc)
        if newacc == [0,0,0]:
            fl = False
            # print(row)
            break
        
    
    if (fl):
        print(n)
		
		
		