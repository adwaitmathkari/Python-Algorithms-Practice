# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 18:45:08 2018

@author: Adwait
"""

def function(array):
    k=2
    while k<= max(array):
        for i in array:
            if i==k:
                k*=2
    return k


"""      
Given a string s, find length of the longest prefix which is also suffix. 
The prefix and suffix should not overlap.
"""

def func2(strin):
    l=len(strin)
    for i in range(1,l//2+1):#i is the length of the string that is measured        
        if strin[0:i]==strin[-i:]:
            maxi=i                
    return maxi
            




def makepalindrome(string): 
    """
    make a palindrome out of given letters if possible
    """      
    adict={}    
    if len(string)==0:
        return 'Empty string'
    #Counter
    for i in string:
        try:
            adict[i]+=1
        except:
            adict[i]=1            
    odd=0
    for i in adict.values():
        if i%2==1:
            odd+=1
    if odd>1:
        return "No Palindrome possible"
    
    else:
#        print('odd,',odd)
        last,first,middle='','',''
        for char in adict.keys():
            if adict[char]%2==1:
                middle=char
                adict[char]-=1
#        print(adict)
        for i in adict.keys():
             for j in range(int(adict[i]/2)):
                 first=first+i
                 last=i+last
        
        return first+middle+last
    