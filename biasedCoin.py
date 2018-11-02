# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 15:14:51 2018

@author: Adwait
"""

import random

def biasedCoin():    
    if random.random() < 0.6:
        return 'HEADS'
    else:
        return 'TAILS'
    
    

 
def fixBiasedCoin(prob):    
    outcome=biasedCoin()
    if prob[0]>0.5:
        if outcome=='HEADS':
            if random.random()<1-0.5/prob[0]:
                outcome=switchOutcome(outcome)
            return outcome
        else:
            return outcome
    else:
        if outcome=='TAILS':
            if random.random()<1-0.5/prob[1]:
                outcome=switchOutcome(outcome)
            return outcome
        else:
            return 'TAILS'
        
        
        
def switchOutcome(astring):
    if astring=='HEADS':
        return 'TAILS'
    elif astring=='TAILS':
        return 'HEADS'
    else:
        return 'invalid string'
    
    
def testCoin(f,prob=None):
    heads=0
    tails=0
    for i in range(1000000):
        if prob!=None:
            astring=f(prob)
        else:
            astring=f()
            
        if astring=='HEADS':
            heads+=1
        else:
            tails+=1
            
#    print('p(heads)= ',heads/100000)
#    print('p(tails)= ', tails/100000)
    return (heads/1000000,tails/1000000)
            
        