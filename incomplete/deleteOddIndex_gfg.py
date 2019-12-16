'''


Some people are standing in a queue. A selection process 
follows a rule where people standing on even positions are selected. 
Of the selected people a queue is formed and again out of these only people 
on even position are selected. This continues until we are left with one person. 
Find out the position of that person in the original queue.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,number of people standing in a queue.

Output:

Print the position(original queue) of that person who is left.

Constraints:

1 ≤ T ≤ 1000
1 ≤ N ≤ 100000000

'''


# for _ in range(5):
        
#     k=int(input())
#     l=[]
#     for i in range(k):
#         l.append(i+1)
#     while len(l)!=1:
#         ldash=[]
#         for i in range(len(l)):
#             if i % 2 == 1:
#                 ldash.append(l[i])
#         l=ldash
#     print(l)

num=2345678
r=1

while num!=1:
    num=num//2
    r=r*2
print(r)




