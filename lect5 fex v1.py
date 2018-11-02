# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:35:16 2017

@author: Adwait
"""

import random
def yieldno():
        while True:
            yield 10
            yield 20
            yield 14
            yield 18
            yield 12
            yield 16
            
k=yieldno()
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
       
    return k.__next__()
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    i=random.randrange(10,21,2)
    return i