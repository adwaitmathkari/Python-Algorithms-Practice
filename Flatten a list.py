# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:56:17 2017

@author: Adwait
"""


def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    def flattensmall(aList):
        lnew=[]
        for x in aList:
            if type(x)==list:
                for n1 in x:
                    lnew+=[n1]
            else: lnew+=[x]
        return lnew
    def islistinlist(aList):
        '''
        Give a list, returns True if there's any element in the list is a list
        '''
        ans=False
        for n in aList:
            if type(n)==list:
                ans=ans or True
        return ans
        
    while islistinlist(aList):
        aList=flattensmall(aList)    
    return aList
