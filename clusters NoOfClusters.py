# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 10:18:04 2018

@author: Adwait
"""
'''
Given a 2D matrix of 0s and 1s, find total number of clusters formed by elements with value 1.  
For example, in the below shown 2D matrix there are total three such clusters. 

This problem is also known as 'Number of Islands' problem.

'''
class point(object):
    def __init__(self,x,y,matrix):
        self.x=x
        self.y=y
        self.matrix=matrix
        self.value=matrix[x][y]
    def equals(self, otherpoint):
        if self.x==otherpoint.x and self.y==otherpoint.y:
            return True
        else:
            return False
   
def NoOfClusters(matrix):
    clusters=[]
    if matrix==[[]]:
        return 0
    rows=len(matrix)
    cols=len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==1:
                clusters.append(clusterListOnePoint(i,j,matrix))
    nomerge=False
    while nomerge==False:
        before=len(clusters)
        for i in clusters:
            for j in clusters:                
                tobreak=mergecluster(i,j,clusters)
                if tobreak:
                    break
        after=len(clusters)
        if before==after:
            nomerge=True
    nomerge=False        
    while nomerge==False:
        before=len(clusters)
        for i,j in clusters:                            
            mergecluster(i,j,clusters)
        after=len(clusters)
        if before==after:
            nomerge=True
            
    return len(clusters) 
 
def clusterListOnePoint(x,y,matrix):
    alist=[]    
    rows=len(matrix)
    cols=len(matrix[0])
    for i in [x+1,x,x-1]:
        for j in [y-1,y,y+1]:
            if 0<=i<rows and 0<=j<cols:
                if matrix[i][j]==1:
                    alist.append(point(i,j,matrix))
    return alist
                
def mergecluster(list1,list2,clusters):
    merge=False
    for point1 in list1:
        for point2 in list2:
            if point1.equals(point2):
                merge=True
    if merge==True:
        clusters.remove(list1)
        clusters.remove(list2)
        mergedlist=[]
        for point in list1:
            mergedlist.append(point)
        for point in list2:
            if all(point.equals(i)==False for i in mergedlist):
                mergedlist.append(point)
        clusters.append(mergedlist)
    return merge