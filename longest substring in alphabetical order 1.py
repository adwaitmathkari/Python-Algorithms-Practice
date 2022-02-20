# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:58:22 2017

@author: Adwait

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', 
then your program should print
"Longest substring in alphabetical order is: beggh"


"""
s='abbdef'
k=len(s)
for n in range(0,k):
    for m in range (n,k):
        count=0
        while s[m]<=s[m+1]:
            count+=1
            maxalph=count
            
        

