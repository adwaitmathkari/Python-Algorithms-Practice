# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 14:48:22 2018

@author: Adwait
"""
def findNos(n):
    """ find numbers in 1 to n where sum of digits of n**2 is equal to no itelf 
    """
    ans = 0
    for i in range(n):
        if (sum([int(i) for i in str(i**2)]) == i ):
            print(i)
            ans+=1
    print('for n = %d, the no of such numbers is %d'% (n,ans))
            
            
    