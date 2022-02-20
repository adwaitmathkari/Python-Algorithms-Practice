# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 11:46:50 2017

@author: Adwait
"""

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

for i in range(20):
    print(deterministicNumber())