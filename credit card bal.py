# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:09:19 2017

@author: Adwait
"""

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

for p in range(1000):
    balance = 5000
    annualInterestRate = 0.2
    itr=0
    while itr<12:
        balance=(balance-p)*(1+annualInterestRate/12)
        itr+=1
    if abs(balance)<6:
        print(p)
    
        
    

        