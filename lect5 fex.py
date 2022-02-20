# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 01:35:16 2017

@author: Adwait
"""

import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    for i in range(20):
        random.seed(i)
        print(i,'  ' ,random.randrange(10,21,2))
    return 'good'
    
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    i=random.randrange(10,21,2)
    return i


def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    i = random.randint(0, 99) 
    if i % 2 == 0:
        return i
    else:
        return genEven()