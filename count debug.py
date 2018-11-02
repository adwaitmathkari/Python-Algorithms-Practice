# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:28:52 2017

@author: Adwait
"""
def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)