# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 14:04:39 2017

@author: Adwait
"""

def getSublists(L, n):
    ans=[]
    
    for ele in range(len(L)-n+1):
        lsub=[]
        for k in range(n):
            lsub=lsub+[L[ele+k]]
        ans=ans+[lsub]
    return ans
        


'''

#code to get ranges instead of lists
def get_ranges(ls):
    N = len(ls)
    while ls:
        # single element remains, yield the trivial range
        if N == 1:
            yield range(ls[0], ls[0] + 1)
            break

        diff = ls[1] - ls[0]
        # find the last index that satisfies the determined difference
        i = next(i for i in range(1, N) if i + 1 == N or ls[i+1] - ls[i] != diff)

        yield range(ls[0], ls[i] + 1, diff)

        # update variables
        ls = ls[i+1:]
        N -= i + 1
        
'''