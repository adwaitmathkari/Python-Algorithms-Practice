# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 03:28:12 2017

@author: Adwait
"""

def recurPower(a, b):
   print(a, b)
   if b == 0:
      return 1
   else:
      return a * recurPower(a, b-1)
#print(recurPower(4,5))


def recurPowerNew(a, b):
   print(a, b)
   if b == 0:
      return 1
   elif b%2 == 0:
      return recurPowerNew(a*a, b/2)
   else:
      return a * recurPowerNew(a, b-1)
  
    
print(recurPowerNew(4,10))