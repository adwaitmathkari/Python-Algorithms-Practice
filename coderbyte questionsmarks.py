# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:33:12 2017

@author: Adwait
"""

"""
Using the Python language, have the function QuestionsMarks(str) 
take the str string parameter, which will contain single digit 
numbers, letters, and question marks, and check if there are
 exactly 3 question marks between every pair of two numbers 
 that add up to 10. If so, then your program should return the 
 string true, otherwise it should return the string false. If 
 there aren't any two numbers that add up to 10 in the string, 
 then your program should return false as well. 

For example: if str is "arrb6???4xxbl5???eee5" 
then your program should return true because there are 
exactly 3 question marks between 6 and 4, and 3 question 
marks between 5 and 5 at the end of the string. 
"""

def QuestionsMarks(s):
    
    ret=True
    count=0
    for i in range(len(s)):
        if s[i] in '123456789':
            noQ=0
            for j in range(i+1,len(s)):
                if s[j]=='?':
                    noQ+=1
                if s[j] in '123457890':
                    if int(s[j])==(10-int(s[i])):
                        count=count+1
                        if noQ==3:
                            ret=ret and True
                        else:
                            ret=ret and False                    
                    break
    if ret==True and count!=0:
        return 'true'
    else:
        return 'false'
    
#QuestionsMarks('abc3??adf?7gjasfjn9?1')
#QuestionsMarks('4?aslfjn??6???3?2???8adfjfhadfoh')           
#QuestionsMarks('a?b?c?1???9????????')
#QuestionsMarks('a?b?c?1???9?1')
#QuestionsMarks('abc3??adf?7gjasfjn9?1')