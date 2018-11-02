# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:06:50 2017

@author: Adwait
"""

def isPalindrome(aString):
    s=aString
    s=s.lower()
    s1=''
    for l in s:
        if l in 'abcdefghijklmnopqrstuvwxyz1234567890':
            s1+=l
    ans=True
    for n in range(len(s1)):
        if s1[n]==s1[len(s1)-1-n]:
            ans=ans and True
        else:
            ans=ans and False
    return ans
        
        