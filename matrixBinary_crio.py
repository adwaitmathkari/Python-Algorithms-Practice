# Problem Description
# Given a sorted matrix, come up with an efficient way to search for a value in the matrix. Each row in the matrix is sorted in ascending order from left to right.
# Each column in the matrix is sorted in ascending order from top to bottom.


import time

def solve(matrix, target):
    if matrix == []:
        return False

    # # raise TypeError(matrix[0])
    # posTargetInRow1 = binarySearchPos(matrix[0], target)
    # # print(posTargetInRow1+1, len(matrix[0])-1 )
    # lastInd = min(len(matrix[0])-1, posTargetInRow1+1)
    rows = len(matrix)
    cols = len(matrix[0])

    if rows > cols:
        
        #binary search on columns
        for col in range(len(matrix[0])):
            ind = binaryCol(matrix, col, target, 0, len(matrix)-1)
            if ind != -1:
                return True
        return False
    else:
        
        for row in range(len(matrix)):
            ind = binary(matrix[row], target, 0, len(matrix[row])-1)
            if ind != -1:
                return True
        return False


def solveOpt1(matrix, target):
    if matrix == []:
        return False


    rows = len(matrix)
    cols = len(matrix[0])

    if rows > cols:
        
        posInCol0 = binaryColPos(matrix, 0, target, 0, len(matrix)-1)
        lastInd = min(posInCol0, len(matrix)-1)
        #binary search on columns
        for col in range(len(matrix[0])):
            ind, found = binaryCol(matrix, col, target, 0, lastInd)
            if found:
                return True
            lastInd = ind
        return False
    else:
        
        # locate after where in the first row the elements are bigger
        # than target and no need to look for after this index in the other rows as well as the
        # elements in those rows after that index will be bigger too
        # this will not really help that much thoug 
        posTargetInRow1 = binarySearchPos(matrix[0], target)
        lastInd = min(len(matrix[0])-1, posTargetInRow1+1)

        for row in range(len(matrix)):
            ind, found = binary(matrix[row], target, 0, lastInd)
            if found:
                return True
            lastInd = ind
        return False


def binarySearch(arr, target):
    return binary(arr, target, 0, len(arr)-1)


def binary(arr, t, l, r):
    m = (l+r)//2
    if l > r:
        return l, False
    if arr[m] == t:
        return m, True
    if t > arr[m]:
        return binary(arr, t, m+1, r)
    else:
        return binary(arr, t, l, m-1)


def binarySearchPos(arr, target):
    return binaryPos(arr, target, 0, len(arr)-1)


def binaryCol(matrix, col, t, l, r):
    m = (l+r)//2

    if l > r:
        return l, False
    if matrix[m][col] == t:
        return m, True
    if t > matrix[m][col]:
        return binaryCol(matrix, col, t, m+1, r)
    else:
        return binaryCol(matrix, col, t, l, m-1)


def binaryPos(arr, t, l, r):
    # print(l,r)
    m = (l+r)//2
    if l > r:
        return l
    if arr[m] == t:
        return m
    if t > arr[m]:
        return binaryPos(arr, t, m+1, r)
    else:
        return binaryPos(arr, t, l, m-1)


def binaryColPos(matrix, col, t, l, r):
    m = (l+r)//2

    if l > r:
        return l, False
    if matrix[m][col] == t:
        return m, True
    if t > matrix[m][col]:
        return binaryCol(matrix, col, t, m+1, r)
    else:
        return binaryCol(matrix, col, t, l, m-1)


def test1():

    # print(binarySearchPos([0,1,10,19,20], 13))

    matrix = [[1,4,7,11,15,18,20], [2,6,8,11,17,18,20], [4,8,8,12,20,22,25], [7,10,11,14,25,29,35], [8, 12, 15, 18, 28, 32,40], [9,13,16,19,29,33,41], [9,13,16,19,29,33,41],[12,18,17,22,31,37,47],[16,19,21,25,37,39,49] ]
    # matrix = [[11,15], [11, 18]]
    # matrix = [[0,0,0],[0,0,0]]
    ts=[12, 4,20,22,14, 5,113,19,32,1234, 0]
    # ts=[0,1,2,3,4,5]
    for t in ts:
        print(t, ':',solve(matrix, t))

    arr = [i for i in range(10000)]
    ts = [-1, 0.5, 167.5, 9999, 9999.5]
    ts = [0, 4, 8, 19999, 199999, 1000, 100000, 9999,
        9998, 123123, 123, 234, 345, 456, 567, 678]
    # for t in ts:
    #     print(binarySearch(arr, t))

    print(binaryCol([[1,7], [2,9], [3,123], [5,1234], [67,1235], [78,1236], [345345, 1231231]], 1, 1234, 0, 6))



def test(solve0):
    f=open('matrixBinary_t1.txt')
    f2 = open('matrixBinary_t1_o.txt')
    nrows = int(f.readline().strip().split(' ')[0])
    matrix = []
    for row in range(nrows):
        matrix.append(list(map(int,f.readline().strip().split(' '))))
    
    nq = int(f.readline().strip())
    counter =0
    unsuccessCount = 0
    t = time.time()
    for q in range(nq):
        counter+=1
        ans = f2.readline().strip()
        if ans=='false':
            ans = False
        else:
            ans = True
        
        calcAns = solve0(matrix, int(f.readline().strip()))
        if ans != calcAns:
            unsuccessCount +=1
            print('unsuccess')
            
        else:
            if counter%1000==0:
                print(ans,calcAns)
        #     # print()
    print(time.time() - t)
    print(unsuccessCount)

# test(solve)
test(solveOpt1)
