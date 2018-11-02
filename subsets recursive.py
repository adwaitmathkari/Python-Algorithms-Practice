# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 02:56:57 2017

@author: Adwait
"""
def genSubsets(l): 
    
    if len(l)==0:
        return [[]]
    
    smaller=genSubsets(l[:-1])
    
    extra=l[-1:]
    new=[]
    for small in smaller:
        new.append(small+extra)
    return smaller+new

print(genSubsets([1,2,3]))
        

#complexity level is 2^n
#in this the functioning is like we call the gensubsets n times each time for
#a smaller list and we finally reach to the len(l)=0 and get that smaller=[]
#now we use this in the line 
#for small in smaller:
#    new.append(small+extra)
#we are doing smaller+new
#which is in fact smaller+(smaller+extra)
#so in [],[1] when we want the next answer we add the next element , 2 , to both these sets
#thus [2],[1,2] and we return [],[1],[2],[1,2]
#next we add 3 to all these [3],[1,3],[2,3],[1,2,3] and return (smaller + new) again
