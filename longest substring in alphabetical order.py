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
letters='abcdefghijklmnopqrstuvwxyz'
k=len(s)
for n in range(26):
    if s[0]==letters[n]: 
        a0=n
    if s[1]==letters[n]: 
        a1=n
    if s[2]==letters[n]:
        a2=n
    if s[3]==letters[n]: 
        a3=n
    if s[4]==letters[n]: 
        a4=n
    if s[5]==letters[n]:
        a5=n
if a5>=a4>=a3>=a2>=a1>=a0:
    print('its in alphabetical order')
else:
    print('not in alphabetical order')

    