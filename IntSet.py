# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:07:20 2017

@author: Adwait
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def intersect(self,other):
        '''returns the intersectin of sets self and other'''
        c=intSet()
        for r in self.vals:
            if r in other.vals:
                c.insert(r)
        return c
    def __len__(self):
        l=len(self.vals)
        return l
    
        
        
        
        
        
        