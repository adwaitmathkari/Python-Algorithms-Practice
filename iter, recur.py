def factorial(a):
    if a==1:
        return 1
    else:
        return a*factorial(a-1)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==1:
        return base
    else:
        return base*iterPower(base, exp-1)
    


def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a==0:
        return b
    elif b==0:
        return a
    elif a>b:
        return gcdRecur(a%b, b)
    elif b>a:
        return gcdRecur(a,b%a)
    elif a==b:
        return a
    