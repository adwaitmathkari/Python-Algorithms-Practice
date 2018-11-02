# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:10:44 2017

@author: Adwait
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    l=[]
    for i in aDict.keys():
        ans= True
        for j in aDict.keys():
            if aDict[i]==aDict[j] and i!=j:
                ans=ans and False
        if ans==True:
            l.append(i)
    return sorted(l)