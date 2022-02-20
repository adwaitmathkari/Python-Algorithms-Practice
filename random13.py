# # if not found:
# #     print('lasdhflasdbf')

# n=6
# board1=[[0]*n for i in range(n)]

# board1[2][3]=1
# # for board in board1:
#     # print(board)

# s='.'*20
# # print(s)

# p='a*b*.*abc*def.t*p*.*'
# i=0
# lim=len(p)
# while i< lim:
#     if p[i]=='*':
        
#         if p[i-1]=='.':
#             p= p[:i-1]+ ':' +p[i+1:]
#         else:
#             p= p[:i-1]+ p[i-1].upper()+p[i+1:]
#         lim-=1
#     else:
#         i+=1
# print(p)


# print(set(list('abcdabc')) in set('abcd'))
# print(set(list('abcdabc')))
# print(set('abcde'))

# for i in range(2):
#     for i in range(6):
#         print(i)

#     print('--', i)


import time

# a=123
# b=23

# print(a if a else 1237489)

# a=[1,2,3,4,5,6,7]
# for j in range(100):
#     print('1', a.pop() if a!=[] else None)

#     print('2', a.pop())

l = range(10000000)
s=set()
for i in l:
    s.add(i)

l2=[]
t= time.time()
for i in l:
    l2.append(i)
print(time.time() - t)


l2=[]
t= time.time()
for key in s:
    l2.append(key)
print(time.time() - t)




