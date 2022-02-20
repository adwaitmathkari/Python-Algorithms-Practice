# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 03:46:44 2017

@author: Adwait
"""
s=input('enter')
string=''
for j in range(4,len(s)-4):
    if s[j] in 'abcdefghijklmnopqrstuvwxyz':
        ans=True
        for k in [j-1,j-2,j-3,j+1,j+2,j+3]:
            if s[k] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                ans=ans and True
            else:
                ans=ans and False
        if s[j-4] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ans=ans and False
        if s[j+4] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            ans=ans and False        
        if ans==True:
            string+=s[j]
                
        
print(string)

##!/usr/bin/env python
##challenge 3
#import urllib2,re
#
#url="http://www.pythonchallenge.com/pc/def/equality.html"
#text = urllib2.urlopen(url)
#contents=text.read()
#
##"One small letter, surrounded by EXACTLY three big bodyguards on each of its
#sides."
#print "".join(re.findall('[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]',contents))