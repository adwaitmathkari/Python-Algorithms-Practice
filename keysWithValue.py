# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:32:18 2017

@author: Adwait
"""

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    ans=[]
    for key in aDict.keys():
        if aDict[key]==target:
            ans=ans+[key]
    ascans=sorted(ans)
    return ascans