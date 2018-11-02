# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:25:47 2017

@author: Adwait
"""

def ispalindrome(s):
    '''
    enter a sentence and see whether it is a palindrome
    '''
    def schar(s):
        ans=''
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                ans=ans+ letter
        return ans
    def ispal(s):
        if len(s)==0 or len(s)==1:
            return True
        else:
            return s[0]==s[-1] and ispal(s[1:-1])
    return ispal(schar(s))

def schar(s):
        ans=''
        for letter in s:
            if letter in 'abcdefghijklmnopqrstuvwxyz':
                ans=ans+ letter
        return ans