# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:04:52 2017

@author: Adwait
"""

print('Please think of a number between 0 and 100!')
m=50
l1=0
l2=100
g='a'
while g!='c':
    print('Is your secret number ', int(m),'?')
    g=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if g=='h':
        l2=m
    elif g=='l':
        l1=m
    elif g!='c':
        print('You should enter h, l or c. Please reenter.')
    m=int(l1/2+l2/2)
print('Game over. Your secret number was: ', int(m))