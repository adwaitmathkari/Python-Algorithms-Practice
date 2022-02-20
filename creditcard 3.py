# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:51:59 2017

@author: Adwait
"""

def yearbalance(balance,annualInterestRate,monthlyPayment):
    '''
    Give initial due to the credit card company(balance), annual interest rate and a 
    fixed monthly payment 
    the fn will return dues at the end of the year
    '''
    itr=0
    while itr<12:
        balance=round((balance-monthlyPayment)*(1+annualInterestRate/12),2)
        itr+=1
        
    return balance

balance=5000
annualInterestRate=0.2

l1=0
l2=balance
p=balance/2

while abs(yearbalance(balance,annualInterestRate,p))>100:
    if yearbalance(balance,annualInterestRate,p)>0:
        l1=p
    else:
        l2=p
    p=(l1+l2)/2

print(p)
    