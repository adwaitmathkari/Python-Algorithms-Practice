# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 12:51:11 2018

@author: Adwait
"""
def simulation():
    import random
    chosen=[]
    l=['r','r','r','g','g','g']
    for ite in [1,2,3]:
        i=random.choice(l)
        l.remove(i)            
        chosen.append(i)
    return chosen


def noReplacementSimulation(numTrials):
    
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    mcs=[]   
    for k in range(numTrials):
        good=0
        trials=3000
        for i in range(trials):
            p=simulation()
            if 'g' not in p or 'r' not in p:
                good+=1
        mcs.append(good/trials)
    return sum(mcs)/len(mcs)

print('simulating monte carlo 100 times, probabilty of 3 red or 3 green balls is:',noReplacementSimulation(100))