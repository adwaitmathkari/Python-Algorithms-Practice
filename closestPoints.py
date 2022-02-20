# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:51:02 2018

@author: Adwait
"""



def dist(p1, p2):
    """p1 p2 are points  
    """
    return ((p1[1]-p2[1])**2 + (p1[0]-p2[0])**2)**.5


def closestPoints(points):
    """
    points is a list of points, sorted bythe x coordinate
    a point is a tuple (x,y)
    the function finds out the pair of pooints which is closest to each other
    it is expected to run in a time complexity of O(n*log(n))
    """

    if len(points)==2:
        return points
    if len(points)==3:
        alist=[points[0],points[1]]
        if dist(points[1],points[2])<dist(alist[0],alist[1]):
            alist[0]=points[2]
        if(dist(points[0],points[2])<dist(alist[0],alist[1])):
            alist=[points[0],points[2]]
    