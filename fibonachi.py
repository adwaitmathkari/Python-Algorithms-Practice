# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 09:48:29 2017

@author: Adwait
"""

def fib(x):
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
for i in range(20):
    print(str(fib(i)))