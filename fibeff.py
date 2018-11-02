# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 12:12:20 2017

@author: Adwait
"""

def fibeff(n,d):
    global noofcalls
    noofcalls+=1
    if n in d:
        return d[n]
    else:
        ans=fibeff(n-1,d)+fibeff(n-2,d)
        d[n]=ans
        return ans
    
d={1:1, 2:2}
noofcalls=0