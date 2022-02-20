def polysum(n,s):
    import math 
    pi=3.14159
    theta=pi/n
    tantheta=math.tan(theta)
    area=0.25*n*s**2/(tantheta)
    perimeter= n*s
    sum1= area+perimeter**2
    ans=int(sum1*10**4)/10**4
    return ans
import math
pi=3.14159
sub=math.tan(pi/4)
print(sub)