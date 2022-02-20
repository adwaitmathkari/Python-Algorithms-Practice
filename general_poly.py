# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:04:30 2017

@author: Adwait
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 
    """
        
    def subpoly(x):
        ans=0
        for n in range(len(L)):
            ans=ans+L[n]*x**(len(L)-n-1)
        return ans
    
    return subpoly