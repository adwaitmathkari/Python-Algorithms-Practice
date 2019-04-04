#python 3.6

"""
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc
"""


"""
natural posn:
    cube turned45 degrees along z axis
equation:
    a= 2**0.5*cos(tx)+sin(tx)
    
    the diagonal plane along xz plane in natural position(as mentioned above) projects a shadow of root2
    this plane when rotates about x axis by theta projects root2*cos(tx)
    
    2 triangles of area 0.5,0.5 project shadows when the cube tilts along the x axis and (0.5+0.5)*sin(tx)

    thus eqn of a=...
    
convert tx into coordinates required:
    
    3 centers to return: (.5,0,0), (0,.5,0), (0,0,.5) make lists for ease
    
    rotate about y axis by 45 degrees
        y axis by 45 degrees
        just x, z coordinates will change
        thus:
            T=45
            x,y,z     go to     (xcosT-zsinT), y, (xsinT+zcosT)
        
    rotate about x axis by tx degrees, tx unknown found by solving eq1
        
        T=solved from eqn
        x,y,z     go to     x, (ycosT-zsinT), (ysinT+zcosT)
        

"""
import math

def dist(v):
    return (v[0]**2+v[1]**2+v[2]**2)**.5

def angle(v1,v2):
    #a dot b= |a|*|b|*cosTheta dot product
    v1dotv2=v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]
    dv1=dist(v1)
    dv2=dist(v2)
    return math.acos(v1dotv2/dv1/dv2)    


def isDistHalf(v):
    d=dist(v)
    return d<.5+10**(-6) and d>.5-10**(-6)


def isAngle90(v1,v2):
    piby2=math.pi/2
    ang=angle(v1,v2)
    delta=10**(-6)
    return ang>piby2-delta and ang<piby2+delta 

# for i in 0,1,2:
#         print("dist %d"%i, end=" ")
#         print(isDistHalf(vertices[i]), dist(vertices[i]), end="---- ")
#     print()    
#     print("angle 01, 02, 12")    
#     print(isAngle90(vertices[0], vertices[1]), end=" ")
#     print(isAngle90(vertices[0], vertices[2]), end=" ")
#     print(isAngle90(vertices[2], vertices[1]), end=" ")

def isAreaA(a, vertices):
    print()


t=int(input())

for x in range(1,t+1):
    print("-------------------------")
    a=float(input())
    
    #if a is 1, then theta is 90 and tan is infinite
    #thus gives zero division error
    if a==1.0:
        print("Case #%d:"%x)
        print(".5 0 0")
        print("0 0 .5")
        print("0 .5 0")
        continue
        
    #vertices
    vertices=[[.5,0,0], [0,.5,0], [0,0,.5]]
    
    #the plane to be projected is a plane at y=-3, parallel to the xz plane
    #thus to get an elongated shadow, first rotating along the z axis 
    # and then along then along the x axis
    #rotating along y axis will not matter
    
    
    #THUS
    #rotate about z axis
    # v[0] is x, v[1] is y and v[2] is z
    #x,y,z     go to     (xcosT-ysinT), (xsinT+ycosT), z
    cos45=math.cos(math.pi/4)
    sin45=math.sin(math.pi/4)
    for v in vertices:
        newv0=v[0]*cos45 - v[1]*sin45
        v[1]=v[0]*sin45 + v[1]*cos45
        v[0]=newv0
    
    
    #now find tx
    #solving for tanTheta after putting into equation for a
    
    delta=8-4*(a**2-1)*(a**2-2)
    b=-2*2**0.5
           
    tantx1=(-b+(delta)**0.5)/(2*a**2-2)
    tantx2=(-b-(delta)**0.5)/(2*a**2-2)
    
    tantx=min(tantx1, tantx2)
#     print("tx values",180/math.pi*math.atan(tantx1),180/math.pi*math.atan(tantx2))
    
    tx=math.atan(tantx)
    
    #rotate along x axis
    #x,y,z     go to     x, (ycosT-zsinT), (ysinT+zcosT)
    
    costx=math.cos(tx)
    sintx=math.sin(tx)
    for v in vertices:
        newv1=v[1]*costx - v[2]*sintx
        v[2]=v[1]*sintx + v[2]*costx
        v[1]=newv1
    
    
    print("Case #%d:"%x)
    print(vertices[0][0],vertices[0][1],vertices[0][2])
    print(vertices[1][0],vertices[1][1],vertices[1][2])
    print(vertices[2][0],vertices[2][1],vertices[2][2])
    
    
    
    
    
    
    