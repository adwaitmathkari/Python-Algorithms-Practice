"""
Problem Description
Given an array A having N elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1.

Input format
The first line contains an integer N denoting the size of the array. The second line contains N space separated positive integers denoting the values in the array A.

Output format
Print N space separated integers, which are the next greater element for each array element. If no such greater element exists for any element, output -1

Constraints
1 <= N <= 10^5

0 <= Values in the array <= 10^9

Sample Input 1
4

1 3 2 4

Sample Output 1
3 4 4 -1

Explanation 1
In the array, the next larger element to 1 is 3 , 3 is 4 , 2 is 4 and for 4, there is no such greater element, hence -1


"""



def nextLargerElement(arr):
    #so go over the next elements and as soon as you find an element that is greater than the current element return it. 
    # so if the array is in descending order then for all elements the answer will be -1
    # if it is in ascending order, then for all elements it will be the immediate next element(except last element of the array)
    # and here
    # [1,3,6,2,4,7,9,12,34,22,21,20,19,18,17,134,3,4,6,23,57,54,43,23]
    # [,-1,-1] 
    # brute force solution
    # ok so for the

    # come in a reverse order
    # add the index of next greatest at each element
    # to find next greatest of any element, jump to the next greatest of the immediate next element until a greater element is found
    # if -1 is encountered at any point then its -1 for this too 

    ln = len(arr)
    nextGreatestIndexArray = [-1]*ln

    for i in range(ln-1,-1,-1):
        if i==ln-1:
            nextGreatestIndexArray[i] = -1
            continue
        if arr[i+1]>arr[i]:
            nextGreatestIndexArray[i] = i+1
        else:
            nextEleIndex = i+1
            while(True):
                if nextGreatestIndexArray[nextEleIndex] == -1:
                    nextGreatestIndexArray[i] = -1
                    break
                if arr[nextGreatestIndexArray[nextEleIndex]] > arr[i]:
                    nextGreatestIndexArray[i] = nextGreatestIndexArray[nextEleIndex]
                    break
                nextEleIndex = nextGreatestIndexArray[nextEleIndex]

    fin = []    
    for ind in nextGreatestIndexArray:

        if ind==-1:
            fin.append(-1)
        else:
            fin.append(arr[ind])
            
    return fin



    
def nextLargerElement2(arr):
    # implement a brute force algo
    pass
    




# n = int(input())
# arr = list(map(int, input().strip().split()))

arr = [1,3,6,2,4,7,9,12,34,22,21,20,19,18,17,134,3,4,6,23,57,54,43,23]
result = nextLargerElement(arr)
print(*arr)
print(*result)
