# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 15:21:03 2018

@author: Adwait

find the sum of all maxpowers of any given prime in a number over a range
Input : L = 1, R = 10, P = 2
Output : 8
There are 10 integers in the range, and:
In 1 the highest power of 2 is 0
In 2 the highest power of 2 is 1
In 3 the highest power of 2 is 0
Similarly the highest powers of 2 in 4, 
5, 6, 7, 8, 9, 10 are 2, 0, 1, 0, 3, 
0, 1 respectively.

Input : L = 10, R = 20, P = 7
Output : 1
There are 11 integers in the range, and:
In 10 the highest power of 7 is 0
In 11 the highest power of 7 is 0
In 12 the highest power of 7 is 0
Similarly the highest power of 7 in 13,
14, 15, 16, 17, 18, 19, 20 and 10 is 0,
1, 0, 0, 0, 0, 0 and 0 respectively.
"""
def highestpower(prime,inte):
    power=0
    ans=0
    while prime**power<=inte:
        if inte%(prime**power)==0:
            ans=power
        power+=1
    return ans
def sumoverrange(prime,r):
    s=0
    for i in r:
        s+=highestpower(prime,i)
        
    return s

def sumoverrange2(prime,r):
    import math
    power=0    
    ans=0
    factorial=math.factorial(max(r))
    while prime**power<=factorial:
        if factorial%(prime**power)==0:
            ans=power
        power+=1
    return ans
    
    
    
    