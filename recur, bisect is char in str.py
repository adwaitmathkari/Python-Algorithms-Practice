# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 10:58:46 2017

@author: Adwait

We can use the idea of bisection search to determine if a character is in a string, 
so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're 
looking for (the "test character"). If they are the same, we are done - we've 
found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the 
middle character. If so, we need only consider the lower half of the string; 
otherwise, we only consider the upper half of the string. 
(Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea 
recursively to test if char is in aStr. char will be a single character and 
aStr will be a string that is in alphabetical order. The function should return
 a boolean value.

As you design the function, think very carefully about what the base cases 
should be.
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    k=len(aStr)
    if k==0:
        return False
    elif k==1:
        if char==aStr:
            return True
        else:
            return False
    elif k==2:
        if char==aStr[0] or char==aStr[1]:
            return True
        else:
            return False
    elif char==aStr[int(k/2)]:
        return True
    elif char<aStr[int(k/2)]:
        aStr=aStr[0:(int(k/2)+1)]
        return isIn(char, aStr)
    else:
        aStr=aStr[int(k/2):]
        return isIn(char, aStr)