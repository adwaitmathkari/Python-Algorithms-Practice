# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 10:49:40 2017

@author: Adwait
"""

num=256
if num<0:
    isneg=True
elif num==0:
    result='0'
    
else:
    result=''
    while num>0:
        result=str(num%2)+result
        num=num//2
print(result)
    