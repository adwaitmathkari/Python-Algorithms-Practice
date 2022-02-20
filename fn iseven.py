# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:54:57 2017

@author: Adwait
"""

def func_a():
    print('inside func_a')
def func_b(y):
    print('inside func_a')
    return y
def func_c(z):
    print('inside func_c')
    return z()

print(func_a())
print(5+func_b(2))
print(func_c(func_a))

