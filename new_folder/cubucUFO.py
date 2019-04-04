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

#def shadow cast by any square on xy plane

def shadowOnXYPlane(p1,p2,p3,p4):
    
    x=[0, p1[0],p2[0],p3[0],p4[0]]
    y=[0,p1[1],p2[1],p3[1], p4[1]]
    
    area=0.5*(x[1]*y[2]+ x[2]*y[3]+ x[3]*y[4]+ x[4]*y[1] -x[2]*y[1] -x[3]*y[2] - x[4]*y[3] -x[1]*y[4])
    return area

print(shadowOnXYPlane((1,0), (1,5), (0,5), (0,0)))
print()


#cube vertices::
# acube is rotated at an angle of 
"""
points 
"""
def 











