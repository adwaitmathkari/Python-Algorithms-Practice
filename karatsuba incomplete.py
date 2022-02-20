# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:47:45 2018

@author: Adwait
"""
#multiplication

def karatsuba(a,b):
    a1=str(a)
    b1=str(b)
    if len(a1)==len(b1)==1:
        return int(a1)*int(b1)
    


