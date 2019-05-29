

def solve (A, N, M, x, sy, sx, y):
    # Write your code here

    # steps array will record the min no of steps each point can be reached in
    # set sx sy to zero,
    # all the points that can be reached from sx sy should be marked as 1
    # these points added to a list
    # next traverse this list and mark all that can be reached from here as 2
    # if the point is found return no of steps
    stepsArray=[[-1]*M for i in range(N)]
    stepsArray[sx][sy]=0

    # to find the points that can be reached from a certain point, 
    # if value of A[i]==10 then ++, +-, --, -+ the values 
    
    l1=nextSetOfPoints(stepsArray, A[sx][sy], sx,sy,N,M)
    
        


def nextSetOfPoints(stepsArray, steps, sx, sy, n, m):
    list1=[]
    prevSteps=steps[sx][sy]
    for i in range(steps+1):
        #i,steps-i need to added or subtracted
        x1=i
        y1=steps-i
        if sx+x1<m and sy+y1<n:
            if stepsArray[sx+x1][sy+y1]==-1:
                list1.append()




T = int(input())
for _ in range(T):
    N, M = map(int, input().split(' '));
    A = []
    for _ in range(N):
        A.append(map(int, input().split(' ')))
    sx, sy = map(int, input().split(' '));
    Q = int(input())

    for _ in range(Q):
        x, y = map(int, input().split(' '))
        solve(A, N, M, x, sy, sx, y)