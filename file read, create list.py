# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 13:58:09 2017

@author: Adwait
"""

data=[]
file_name=input('enter a filename')

try:
    fh=open(file_name, 'r')
except IOError:
    print('cannot open file', file_name)
else:
    for new in fh:
        print(new)
        print('90')
        if new!='\n':
            addIt=new[:-1].split(',')
            print(addIt)
            data.append(addIt)

finally:
    fh.close()
    
print(data)