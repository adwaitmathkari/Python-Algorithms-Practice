# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 13:17:27 2017

@author: Adwait
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try: 
        div=item / denom
        return div
    except ZeroDivisionError:
        return 0
        
        