# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 13:43:11 2018

@author: Adwait
"""

#recursive code
"""
Given a sorted array of integers containing duplicates, write a program which returns the last index of an element.

Example:
Input:
list = [0, 1, 2, 2, 4, 5, 5, 5, 8}]
num = 5
Output: 
Element 5 found at index 7
"""
count=0
def lastIndexOf(n,alist):
    if n not in alist:
        return 'Error no. not in list'
    if alist[len(alist)-1]==n:
        return len(alist)-1
    for i in range(len(alist)-1):        
        if alist[i]==n and alist[i+1]!=n:
            return i
            
       
def lastIndexOfv2(n,alist):
    global count
    count+=1
    l=len(alist)
    if l==0:
        return -1
    if l==1:
        if alist[0]==n:
            return 0
        else:
            return -1
    if alist[l//2]<=n:
        return l//2+lastIndexOfv2(n,alist[l//2:])
    elif alist[l//2]>n:
        return lastIndexOfv2(n,alist[:l//2])
    
def test(n,alist):
    v1=lastIndexOf(n,alist)
    v2=lastIndexOfv2(n,alist)
    print(v1)
    print('v2', v2)    
    return v1==v2