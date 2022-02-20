# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 21:57:41 2017

@author: Adwait
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    ans=0
    for l in aDict.values():        
        ans=ans+len(l)
    return ans
