"""
    a cube of length 1x1x1
    centre is fixed at 0,0,0
    it can rotate in any direction
    sun is beaming from the top on the x-y plane
    find the position of the cube such that it casts a shadow of of area 'A' on the same plane
    return the coordinates of the centres of 3 non parallel faces of the cube
    ( the area should be A-10^-6 to A+10^6, 
      dist from each pt to origin must be 0.5+-10^-6
      and the angle bet segments connecting points and origin must be pi/2 +- 10^-6 radian)    
"""


import math
#def shadow cast by any square on xy plane

def shadowOnXYPlane(p1,p2,p3,p4):
    
    x=[0, p1[0],p2[0],p3[0],p4[0]]
    y=[0,p1[1],p2[1],p3[1], p4[1]]
    
    area=0.5*(x[1]*y[2]+ x[2]*y[3]+ x[3]*y[4]+ x[4]*y[1] -x[2]*y[1] -x[3]*y[2] - x[4]*y[3] -x[1]*y[4])
    return area

print(shadowOnXYPlane((1,0), (1,5), (0,5), (0,0)))

#cube vertices::
# acube is rotated at an angle of 

"""
SOLUTION RW
thus there are 3 variables in total as you can turn the cube in 3 planes in some angles
rotating along z axis will not affect the area
thus only 2 variables
further the long planar diagonal will project the area on the x-y plane
thus it is a simple cosine of the angle that the long diagonal has turned

"""


# finding area when 
# the cube is turned 45deg from x towards z
# and then then x towards z 
# only rotating along the x-z plane:
 
def area(txz):
    """
    txz is thetaxz goes from 0 to pi 
    original vertices in the xz plane are +-0.5, +-0.5
    and their shadow falls from -0.5 to +0.5 and shadow area= (0.5-(-0.5))*1 = 1
    """
    xProjections=[0.5,0.5,-.5,-.5]
    vertices=[(0.5,-0.5),(.5,.5), (-.5,.5), (-.5,-.5)]  
    #newXPr is the new projection of the x coordinate of 4 vertices of square seen from side view
    #formula given rotate by theta(T): x= x1cosT-y1sinT
    newXPr=[(lambda x: (x[0]*math.cos(txz)- x[1]*math.sin(txz)))(p) for p in vertices]
    #returns the area as 1*(the diff between ending vertices as area)
    return max(newXPr)-min(newXPr)


print(area(0))
print(area(math.pi/4))
print(area(math.pi))

#better def of area when rotating only only about Y axis 
#    take the projection of the long diagonal plane
#    

def areaTwoRotations(txz, tyz):
    
    """
    area projected when rotation about y axis-- txz    and that about x axis-- tyz
    """
    pass
"""
thus to get area between 1 and 1.41:
    we have a simple rotation of the cube and the equation will be in simple terms of  ty(alias txz)
    consider natural posn as rotated at 45deg
    eq:
        a=2**0.5*(cos(ty))
    
    
further rotation around x axis
    if tx is 90 deg area is 1, tx is 0 deg area is root2 and if tx is 35.2641 deg, area is 1.732
    ty=0 deg
    eq
        a=2**0.5*cos(tx)+(0.5+0.5)*sin(tx)
    
"""
def solution(area):
    pass

print(2**0.5*math.cos(.6154)+math.sin(0.6154))

