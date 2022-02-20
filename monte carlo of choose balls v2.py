# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:51:11 2018

@author: Adwait
"""
import random

def noReplacementSimulation(numTrials):
    
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    def simulation1():        
        chosen=[]
        l=['r','r','r','g','g','g']
        for ite in [1,2,3]:
            i=random.choice(l)
            l.remove(i)
            chosen.append(i)
        return chosen
    mcs=[]
    good=0
    for i in range(numTrials):
        p=simulation1()
        if ('g' not in p) or ('r' not in p):
            good+=1
        
    mcs.append(good/numTrials)
    return sum(mcs)/len(mcs)

print('simulating monte carlo 20 times, probabilty of 3 red balls is:',noReplacementSimulation(5000))