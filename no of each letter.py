# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:23:10 2017

@author: Adwait
"""
#no of letters
text=input('enter your text')
l='abcdefghijklmnopqrstuvwxyz'
d={}
s=''
for let in l:
    d[let]=0
for let in text:
    if let in l:
        s+=let
for let in s:
    d[let]+=1
d2={}
d3=dict(d)
while len(d3)>0:
    p=-1
    pkey=''
    for let in d3.keys():
        if d3[let]>p:
            p=d3[let]
            pkey=let
    d2[pkey]=d3[pkey]
    del d3[pkey]
    
    
print(d2)