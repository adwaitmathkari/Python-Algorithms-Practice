# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:47:05 2017

@author: Adwait
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    for l in aDict.keys():
        if aDict[l]==max(aDict.values()):
            return l