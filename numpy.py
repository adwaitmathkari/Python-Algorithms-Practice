# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 16:23:47 2018

@author: Adwait
"""

import numpy as np
import matplotlib.pyplot as plt

a=np.linspace(1,3,10)
print(a)
#[ 1.          1.22222222  1.44444444  1.66666667  1.88888889  2.11111111
#  2.33333333  2.55555556  2.77777778  3.        ]

b=np.array([(1,2,3),(3,4,5), (78,3,4)])
print(b)
#[[ 1  2  3]
# [ 3  4  5]
# [78  3  4]]

#def stdDevOfLengthskiwi(L):
#    """
#    L: a list of strings
#
#    returns: float, the standard deviation of the lengths of the strings,
#      or NaN if L is empty.
#    """
#    import numpy as np
#    return float(np.std(np.asarray([len(i) for i in L]))) if L else float('NaN')

c=np.asarray([len(i) for i in ['abcdge','alnacln','akjnakjnec']])
print(c)
#[ 6  7 10]
np.std([1,3,5,6,7,4,123,34])
#Out[137]: 39.107024624739736
#is for standard deviation of a list 
c.max()
#10
c.sum()
#23

b=np.array([(1,2,3),(3,4,5), (78,3,4)])
print(b)
#[[ 1  2  3]
# [ 3  4  5]
# [78  3  4]]
#axis 0 are the columns
#axis 1 re the rows
b.sum(axis=0)
#array([82,  9, 12])
b.sum(axis=1)
#array([ 6, 12, 85])

d=np.asarray([(4,25,49), (1,3,7), (36,54,99)])
print(np.sqrt(d))

#[[ 2.          5.          7.        ]
# [ 1.          1.73205081  2.64575131]
# [ 6.          7.34846923  9.94987437]]

f1=np.array([0,1,2,3,4,5])
f=np.asarray([i**2 for i in range(6)])
g=np.asarray([i**3 for i in range(6)])
print(np.vstack((f1,f,g)))

#[[  0   1   2   3   4   5]
# [  0   1   4   9  16  25]
# [  0   1   8  27  64 125]]

np.hstack((f1,f,g))

#array([  0,   1,   2,   3,   4,   5,   0,   1,   4,   9,  16,  25,   0,
#         1,   8,  27,  64, 125])

d.ravel()
#array([ 4, 25, 49,  1,  3,  7, 36, 54, 99])

print(np.arange(0,np.pi,0.1))
#[ 0.   0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4
#  1.5  1.6  1.7  1.8  1.9  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9
#  3.   3.1]


x=np.arange(0,2*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()
#shows a sin wave


print(np.exp(f1))

#[   1.            2.71828183    7.3890561    20.08553692   54.59815003
#  148.4131591 ]
