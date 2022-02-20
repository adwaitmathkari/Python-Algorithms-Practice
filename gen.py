# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 19:11:03 2017

@author: Adwait
"""

import math


def polysum(n,s):
    """polygon has n number of sides. Each side has length s"""
    
    #Calculating area of polygon
    area = ((0.25*n*(s**2)))/(tan(pi/n))
    perimeter = n*s
    
    sum = area + perimeter**2
    
    return round(sum,4)