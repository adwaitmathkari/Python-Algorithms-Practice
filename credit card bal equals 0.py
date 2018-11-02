# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:09:19 2017

@author: Adwait
"""

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

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


    
balance = 999999
annualInterestRate = 0.18

#using bsection in limits 0 and balance to find p(monthlly payment) which will give zero dues at the end of the year
l1=0
l2=balance*((1 + annualInterestRate/12)**12)/12.0
p=l1/2+l2/2

while abs(yearbalance(balance, annualInterestRate, p))>.01:
    
    if yearbalance(balance, annualInterestRate,p)>0:
        l1=p
    else:
        l2=p
    p=l1/2+l2/2
    
    
print('Lowest Payment: ', round(p,2))