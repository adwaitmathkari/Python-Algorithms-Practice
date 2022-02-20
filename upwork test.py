# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 01:15:08 2018

@author: Adwait
"""

print("\x48\x49!")
HI!

def f(x):
    return x%2!=0 and x%3!=0


result=filter(f,range(20))

result
Out[6]: <filter at 0x2bc65db7f0>

print(result)
<filter object at 0x0000002BC65DB7F0>

for i in result:
    print(i)
    
1
5
7
11
13
17
19

s=[]

for x in range(5):
    s.append(lambda: x**2)
    

x=8

t=(1,2,3)

enumerate(t)
Out[13]: <enumerate at 0x2bc65faee8>

for i,v in enumerate(t):
    print(i,v)
    
0 1
1 2
2 3

t=(1,2,3,4,5)

t[1:3]
Out[16]: (2, 3)

x=15

y=45

res=x if x<y else y

res
Out[20]: 15