"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

"""
# iterations
# backtracking?
# [1,3,3,6,2,4,2,2,2,2,2,3,2,3,1] 
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps=0
        i=0
        ln=len(nums)
        while i<ln-1:   

            maxNext=0
            
            for j in range(i, i+nums[i]+1):
                # print(j)
                if j==ln-1:
                    nextI=j
                    break
                if j+nums[j] > maxNext:
                    maxNext = j+ nums[j]
                    nextI = j
            
            i=nextI
            steps+=1
            
        return steps

s=Solution()
# nums = [1,3,2,1,1,4,2,2,3,1,1,1,2,2]
# print(s.jump(nums))

for i in range(5):
    ln=int(input('input ln'))
    nums1=[]
    for j in range(ln):
        nums1.append(int(input('inputelement ')))
    print('--------------------- no of steps for ', nums1)
    print(s.jump(nums1))
print()