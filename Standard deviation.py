# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:27:36 2018

@author: Adwait
"""

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L==[]:
        return float('Nan')
    l=[]
    for i in L:
        l.append(len(i))
    mean=sum(l)/len(l)
    alist=[]
    for i in l:
        alist.append((mean-i)**2)
    variance=sum(alist)/len(alist)
    stdDev=variance**0.5
    return stdDev
    
        
def stdDevOfLengthskiwi(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import numpy as np
    return float(np.std(np.asarray([len(i) for i in L]))) if L else float('NaN')