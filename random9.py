# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:28:24 2018

@author: Adwait
"""

import numpy as np
#a=np.empty((20,6),['str',])
#a[0][0]='Position'
#a[0][1]='Team'
#a[0][2]='Played'
#a[0][3]='Won'
#a[0][4]='Draws'
#a[0][5]='Points'
flist=[]
for i in range(10):
    alist=[]
    for j in range(5):
        alist.append(i*j)
    flist.append(alist)
flist.insert(0,['Position','Team','Played','Won','Draws'])    
a=np.array(flist)
print(a)