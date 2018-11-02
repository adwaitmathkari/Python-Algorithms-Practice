# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 12:45:41 2018

@author: Adwait
"""

"""
Given an array of n integers(duplicates allowed). 
Print “Yes” if it is a set of contiguous integers else print “No”.


INPUT: The first line consists of an integer T i.e. the number of test cases. 
First line of each test case consists of an integer n, denoting the size of array. 
Next line consists of n spaced integers, denoting elements of array.


OUTPUT:  Print “Yes” if it is a set of contiguous integers else print “No”.
"""

def isContiguous(array):    
    l=[]
    for i in array:
        l.append(int(i))
    l1=sorted(l)
    tocheck=range(l1[0],l1[-1]+1)
    ans=True
    for i in tocheck:
        if i in l1:
            ans=ans and True
        else:
            ans=ans and False
    if ans==True:
        return "Yes"
    else:
        return "No"
    
sample=input()
mainlist=[]
l=[]
mainlist=sample.split('\n')
mainlist2=[]
for i in mainlist:
    k=i.split(" ")
    mainlist2.append(k)


for i in range(1,len(mainlist2)):
    if i%2==0:
        print(isContiguous(mainlist2[i]))
        
