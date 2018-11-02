# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 01:19:41 2018

@author: Adwait
"""
class Matrix(object):
    def __init__(self, matrix):
        self.matrix=matrix
        self.rows=len(matrix)        
        self.cols=len(matrix[0])
        self.checked=[]
        for i in range(self.rows):
            alist=[]
            for j in range(self.cols):                            
                alist.append(False)
            self.checked.append(alist)
#        self.clusters=[]
    
    def allchecked(self):
        ans=True
        for i in range(self.rows):
            for j in range(self.cols):
                ans=ans and self.checked[i][j]
        return ans
        
        
def NoOfClusters(matrix):
    m=Matrix(matrix)
    clusters=[]
    if matrix==[[]]:
        return 0    
    while not m.allchecked():
        for i in range(m.cols):
            for j in range(m.rows):
                if m.matrix[j][i]==1 and m.checked[j][i]==False:
                    cluster=[]
                    addAdjacent(i,j,m,cluster)
                    clusters.append(cluster)
                    
    print(clusters)
    return len(clusters)
    

def addAdjacent(x,y,m,alist):
    if m.checked[y][x]==False:        
        alist.append((x,y))
        m.checked[y][x]=True
    for i in [x+1,x,x-1]:
        for j in [y-1,y,y+1]:
#            print(i,',',j)
            if 0<=i<m.cols and 0<=j<m.rows:
#                print(i,',',j)
#                print(m.checked)                
                if m.matrix[j][i]==1 and m.checked[j][i]==False:
                    alist.append((i,j))
                    m.checked[j][i]=True
                    addAdjacent(i,j,m,alist)
                else:
                    m.checked[j][i]=True
                    
                    
                    
                    
                    
                    
                    
                    