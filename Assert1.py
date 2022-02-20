# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:06:59 2017

@author: Adwait
"""

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        print(numbers[i])
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers