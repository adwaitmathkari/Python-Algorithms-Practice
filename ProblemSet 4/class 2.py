# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:54:43 2017

@author: Adwait
"""

class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
        
#class Clock(object):
#    def __init__(self, time):
#        self.time = time
#    def print_time(self, time):
#        print(time)
#    def __str__(self, time):
#        return (str(self.time))

#clock = Clock('5:30')
#clock.print_time('10:30')