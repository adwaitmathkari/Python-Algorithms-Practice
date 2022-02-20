

"""
Problem statement:

sort a given list so that the even indices are all the largest nos of the list sorted in descending order 
and the odd indices are the rest sorted in ascending order.

The sorting should happen in place


for ex.
[1,4,8,3,7,10,19,13,12,6]->[19,1,13,3,12,4,10,6,8,7]

"""

# so
# for odd index, l[i]> l[i-1] implies swap as the odd index cannot be greater than the even index before obviously
# for enen index, it cannot be smaller than the previous odd index

# 1 4 8 3 7 10 
# 4 1 
# 8 1 4
# 8 1 4 3 
# 8 1 7 3 4 
# 8 1 7 3 10 4 


#1 3 4 7 8 10
# 1 
# 3 1 
# 4 1 3 
# 7 1 4 3 
# 8 1 7 3 4
#  

"""
Given an array Arr[] of N distinct integers, print the array in such a way that the first element is 
first maximum and second element is first minimum and so on.

Input:
First line of input contains a single integer T which denotes the number of test cases. 
Then T test case follows. First line of each test case contains a single integer N which denotes 
the number of elements in the array. Second line of each test case contains N space separated integers.

Output:
For each test case print the given array in such a way that the first element is 
first maximum and second element is first minimum and so on.

Constraints:
1<=T<=100
1<=N<=104
1<=Arr[i]<=105

"""

# sorted array
# all evens are greater than all the odds
# odd length array-- next is the biggest and need to be sent to the first indexby flipping alternate nos till the first index is reached
# even length array-- next is bigger needs to be flipped with last and then the even array should be fixed.


class Solution:
    def sortArray(self,arr):
        for i in range(len(arr)):
            if i%2 == 0:
                self.swapToFirst(arr, i)
            else:
                self.swap(arr, i, i-1)
                self.swapToFirst(arr, i-1)
        return arr
    def swapToFirst(self, arr, ind):
        for i in range(ind, 1, -2):
            # swap ind and ind-1
            arr[i], arr[i-2] = arr[i-2], arr[i]
            # self.swap(arr,i,i-2)

    # def swap(self, arr,i,j):
    #     temp=arr[i]
    #     arr[i]=arr[j]
    #     arr[j]=temp


s=Solution()

# t = int(input())
# for _ in range(t):
#     length = int(input())
#     arr = list(map(int, input().split()))
#     s.sortArray(arr)
#     for i in range(len(arr)-1):
#         print(arr[i], end=" ")
#     print(arr[len(arr) -1])
    

print(s.sortArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))


