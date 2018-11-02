# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 16:32:59 2017

@author: Adwait
"""

x=0.5
l1=x
l2=1
epsilon = 0.01
step = 0.1
guess = (l1+l2)/2
itr=0
while abs(guess**2-x) >= epsilon:
    if guess**2 > x:      
        l2=guess        
    else:        
        l1=guess        
    itr+=1
    guess=l1/2+l2/2
    
if abs(guess**2 - x) >= epsilon:
    print('failed', str(guess))
else:
    print('succeeded: ' + str(guess)+ '  iterations:  '+ str(itr))
    