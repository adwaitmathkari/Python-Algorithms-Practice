# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 19:29:10 2016

@author: ericgrimson
"""

def fib(n):
    global callsininefficient
    callsininefficient+=1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


