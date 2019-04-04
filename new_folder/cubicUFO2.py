"""
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc"
"""


"""
natural posn:
    cube turned45 degrees along y axis
equation:
    a= 2**0.5*cos(tx)+sin(tx)

convert tx into coordinates required:
    
    3 centers to return: (1,0,0), (0,1,0), (0,0,1) make lists for ease
    
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

t=int(input())

for x in range(1,t+1):
    
    a=int(input())
    
    #if a is 1, then theta is 90 and tan is infinite
    #thus gives zero division error
    if a==1:
        print("Case #%d"%x)
        print("1 0 0")
        print("0 0 1")
        print("0 1 0")
        
    #vertices
    vertices=[[1,0,0], [0,1,0], [0,0,1]]
    
    #rotate about y axis
    # v[0] is x, v[1] is y and v[2] is z
    #x,y,z     go to     (xcosT-zsinT), y, (xsinT+zcosT)
    cos45=math.cos(math.pi/4)
    sin45=math.sin(math.pi/4)
    for v in vertices:
        v[0]=v[0]*cos45 - v[2]*sin45
        v[2]=v[0]*sin45 + v[2]*cos45
    
    
    #now find tx
    #
           
    tantx1=(2*2**0.5+(8-4*(a**2-1)*(a**2-2))**0.5)/(2*a**2-2)
    tantx2=(2*2**0.5-(8-4*(a**2-1)*(a**2-2))**0.5)/(2*a**2-2)
    
    tantx=max(tantx1, tantx2)
    
    tx=math.atan(tantx)
    
    #rotate along x axis
    #x,y,z     go to     x, (ycosT-zsinT), (ysinT+zcosT)
    
    costx=math.cos(tx)
    sintx=math.sin(tx)
    for v in vertices:
        v[1]=v[1]*costx - v[2]*sintx
        v[2]=v[1]*sintx + v[2]*costx
    print("Case #%d"%x)
    print(v[0])
    print(v[1])
    print(v[2])
    
    
    
    
    
    
    