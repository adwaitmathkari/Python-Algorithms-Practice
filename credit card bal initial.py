# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:09:19 2017

@author: Adwait
"""
# given values
# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

def yearbalance(balance,annualInterestRate,monthlyPayment):
    itr=0
    while itr<12:
        balance=round((balance-monthlyPayment)*(1+annualInterestRate/12),2)
        itr+=1
        
    return balance
	      
monthlyPayment=0        
while yearbalance(balance,annualInterestRate,monthlyPayment)>0:    
    monthlyPayment+=10
print('Lowest Payment: ', monthlyPayment)
            