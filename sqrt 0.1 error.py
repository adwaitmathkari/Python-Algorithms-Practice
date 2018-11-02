# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 19:09:26 2017

@author: Adwait
"""
itr=0
while itr<3:
    x=float(input('enter a no '))
    ans=0.0 
    while ans*ans<x:
        ans=ans+0.1
    
    if int(ans*ans)==x: 
        print(str(ans)+ 'is the root of'+ str(x) )
    else : 
        print(str(x) + 'is not a perfect square but its root is'+ str(ans-0.05))
    itr+=1
    