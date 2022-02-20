# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:34:21 2017

@author: Adwait
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp=0
    while base**exp<num:
        exp+=1
    if num-base**(exp-1)<=base**exp-num:
        return exp-1
    else:
        return exp