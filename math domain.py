def polysum(n,s):
    import math 
    pi=math.pi
    theta=pi/n
    tantheta=math.tan(theta)
    area=0.25*n*s**2/(tantheta)
    perimeter= n*s
    sum1= area+perimeter**2
    ans=round(sum1,4)
    return ans
