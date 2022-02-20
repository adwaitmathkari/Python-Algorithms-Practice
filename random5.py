# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 03:36:33 2017

@author: Adwait
"""

dicti={}
s=input('enter')
for j in s:
    if j in dicti.keys():
        dicti[j]+=1
    else:
        dicti[j]=1
d2=dict(dicti)
l=[]
for k in dicti.keys():
    l.append([k,dicti[k]])
    