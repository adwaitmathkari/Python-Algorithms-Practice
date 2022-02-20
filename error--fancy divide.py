# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 03:04:57 2017

@author: Adwait
"""

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
    return list_of_numbers

fancy_divide([0, 2, 4], 1)
        
#def fancy_divide(list_of_numbers, index):
#    try:
#        try:
#            denom = list_of_numbers[index]
#            for i in range(len(list_of_numbers)):
#                list_of_numbers[i] /= denom
#        finally:
#            raise Exception("22")
#    except Exception as ex:
#        print(ex)
#    return list_of_numbers
#
#fancy_divide([0, 2, 4], 4)


#n=53
#
#try:
#    # raise Exception("5")
#    try:
#        raise Exception('abcde',n,n,n,n,n,n,n)
#    # except ZeroDivisionError:
#    #     print('nothing')
#    finally:
#        #a = 1/0
#        print('finally')
#except Exception as abcde:
#    print('yes ', abcde)


#def fancy_divide(list_of_numbers, index):
#    try:
#        denom = list_of_numbers[index]
#        for i in range(len(list_of_numbers)):
#            list_of_numbers[i] /= denom
#    except:
#        raise Exception("some error occured maybe you are dividing by zero or maybe your index is out of range of the list")
#        
#    return print(list_of_numbers)
#
