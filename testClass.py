# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 13:32:00 2018

@author: Adwait
"""
def fn1():

    
    n=int(input())
    adict={}
    for i in range(n):
        comp=input()
        if (comp in adict.keys()):
            adict[comp] +=1
        else:
            adict[comp]=1
    #print(adict)
    maxlist=[]
    for company in adict.keys():
    #    print(c6ompany)
        if (maxlist==[]):
            maxlist.append(company)
            maxlist.append(adict[company])
            
        if ((adict[company]>maxlist[1]) or (adict[company]==maxlist[0] and company>=maxlist[0])):
            maxlist[0]=company
            maxlist[1]=adict[company]
    #    print(maxlist)
    print(maxlist[0])
    
def fn2():
    n=input()
    arr=(input()).split()
    l=[]
    for i in arr:
        l.append(int(i))
    nops=int(input())   
    for i in range(nops):
        denom=int(input())
        for i in range(len(l)):
            l[i]=l[i]//denom
    s=""
    for i in l:
        s+=str(i)+" "
       
    print(s)        
