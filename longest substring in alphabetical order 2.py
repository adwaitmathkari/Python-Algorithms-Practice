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
s='ashvbasdvhabcdefghijklmnopaskjdbasdgashjaaaabbbbcdeeeefghijklmnopqrstuvw'
k=len(s)
maxstring=''
m=0
while m<k-1:
    p=''
    for n in range(m,k-1):
        
        if s[n]<=s[n+1] and n!=k-2:
            
            p=p+s[n]
        elif s[n]<=s[n+1] and n==k-2:
            
            p=p+s[n]+s[n+1]
            if len(p)>len(maxstring):
                maxstring=p
            break
        else:
            p=p+s[n]
            if len(p)>len(maxstring):
                maxstring=p
            break
        
    m=m+1
print(maxstring)