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
s='abcdefkdsbkjjjjjjjjjjjjkkkabcdefghijklmnoopkklllllasffhaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1a'
k=len(s)
maxstring=''
m=0
while len(s)!=0:
    k=len(s)
    p=''
    for n in range(0,k-1):        
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
    s=s[1:]
print('Longest substring in alphabetical order is: ', maxstring)