# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 21:05:02 2017

@author: Adwait
"""

class coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self, other):
        xDiffSq= (self.x-other.x)**2
        yDiffSq=(self.y-other.y)**2
        return (xDiffSq+yDiffSq)**.5
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def __sub__(self,other):
        return coordinate(self.x-other.x,self.y-other.y)
    def __add__(self,other):
        return coordinate(self.x+other.x,self.y+other.y)        
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        ans='coordinate(%s,%s)'%(self.x,self.y)
        return ans
   
#NOTE
#eval(repr(c)) == c gives True 
        
    
        
    
