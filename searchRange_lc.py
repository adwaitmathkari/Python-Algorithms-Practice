
"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""


class Solution:
    def searchRange(self, nums, target):
        ln = len(nums)
        right = self.binaryRight(nums, target, 0, ln-1)
        left = self.binaryLeft(nums, target, 0, ln-1)
        return [left, right]

    def binaryRight(self,arr, t, l, r):
        m = (l+r)//2
        if l > r:
            return -1
        if arr[m] == t:
            if m == len(arr)-1:
                return m
            if arr[m+1] != t:
                return m
            return self.binaryRight(arr, t, m+1, r)            
            
        if t > arr[m]:
            return self.binaryRight(arr, t, m+1, r)
        else:
            return self.binaryRight(arr, t, l, m-1)


    def binaryLeft(self, arr, t, l, r):
        m = (l+r)//2
        if l > r:
            return -1
        if arr[m] == t:
            if m == 0:
                return m
            if arr[m-1] != t:
                return m
            return self.binaryLeft(arr, t, l, m-1)
            
        if t > arr[m]:
            return self.binaryLeft(arr, t, m+1, r)
        else:
            return self.binaryLeft(arr, t, l, m-1)


numss=[[0,0,1,2,2,2,2,3,4,5,6,6,7], [1,2,2,2,2,2,2,2,2,2,3], [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10]]


for nums in numss:
    print(Solution().searchRange(nums, 6))

