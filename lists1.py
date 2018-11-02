# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:48:19 2017

@author: Adwait
"""
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total=0
for i in l:
    total+=i
print(total)


m=[]
for i in range(20):
    m.append(i)


'''

#append will be very useful while storing values like a1 a2 a3 a4 a5 a6 etc....


''' 
    
print('m')    
print(m)
print('l')
print(l)
j=m+l
print('j=m+l')
print(j)


g=[1,2,3,4,5,6,7,8,9,10]
print(g[0], g[1], g[2])

for i in g:
    if i%2==1:
        g.remove(i)
        #removes that specific element
        # if element occurs more than once removes only the first instance

    
print("g is", g)

g.pop()

#removes the last element from the list and gives it back

print('now g is', g)



s='i <3 cs'
list('s')
print(list(s))
l3=s.split('<')
print('l3', l3)

L=['a', 'b', 'c', 'd', 'e']

s4=''.join(L)
s5='_'.join(L)

print('s4 is ', s4, 's5 is ',s5)
s6=',,'.join(L) 
# returns 'a,,b,,c,,d,,e''


k=[1,3,5,2,4,7,8,9,3]

p=sorted(k)#p is k in a sorted manner

print('k', k)
print('p', p)

k.sort()#changes k directly and sorts it
print(k)

k.reverse()#reverses the order of k
print(k)

'''
note that the functions like l.append, l.sort , l.reverse,directly change the list
'''