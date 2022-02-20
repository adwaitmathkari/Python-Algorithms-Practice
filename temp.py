# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
name adwait 
"""

#import string

#s1=string.ascii_lowercase

def maxalphstring(aString):    
    s=aString
    k=len(aString)
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
        return maxstring
    
s='abcdefghijklakfjhsadkjh'
print('Longest substring in alphabetical order in', s ,'is: ', maxalphstring(s))




def maxalphstringv2(aString):    
    s=aString
    k=len(aString)
    maxstring=''
    m=0
    while m<=k-1:
        p=''
        for n in range(m,k):
            if n==k-1:
                p=p+s[n]                
            elif s[n]<=s[n+1]:                
                p=p+s[n]                
            else:                
                break
        if len(p)>len(maxstring):
                    maxstring=p
        m=m+1
        return maxstring
    