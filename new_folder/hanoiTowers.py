
def shift(tower1, tower2):
    #shift ring from tower1 to ttower 2
    #ring on tower2 must be bigger than the one on tower 1
    if(tower1==[]):
        print("tower1 is empty")
        return
    if(tower2==[] or tower1[-1]<tower2[-1]):
        tower2.append(tower1.pop())
        
"""
A is the FROM tower
B is the TO tower
C is the additional tower
"""
def solveHanoi(n, A, B, C):
    if(n==1):
        shift(A,B)     
        return
    solveHanoi(n-1, A, C, B)
    shift(A,B)
    solveHanoi(n-1, C, B, A)
    return

A, B, C= [i for i in range(20,0,-1)], [], []
print(A,B,C)
solveHanoi(20,A, B, C)
print(A,B,C)
    

