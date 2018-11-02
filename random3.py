# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:04:01 2017

@author: Adwait
"""

def bisectSearch(l,e):
    if len(l)==0:
        return False
    elif len(l)==1:
        return l[0]==e
    half=len(l)//2
    if e<l[half]:
        return bisectSearch(l[:half],e)
    else:
        return bisectSearch(l[half:],e)
    
    
bisectSearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],12)