"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

from typing import List

class Solution:
    def swap(self, list, i,j):
        temp=list[i]
        list[i]=list[j]
        list[j]=temp

    
    def nextPermutation(self, nums: List[int]) -> None:

        lnums=len(nums)
        found = False
        for i in range(lnums-1, 0,-1):
            if nums[i]>nums[i-1]:
                index = i
                found =True
                break
        
        if not found:
            for i in range((lnums+1)//2 ):
                self.swap(nums, i, lnums-1-i)
        else:
            #length will be lnums-index thus by prev logic, that+1 // 2 times the swapping should occur
            #thus range (lnums-index+1) // 2 from index thus index, index+that2  
            nswaps=lnums-index+1
            nswaps=nswaps//2
            for i in range(index, index+nswaps):
                # print(i, lnums-1-(i-index))
                self.swap(nums, i, lnums-1-(i-index))
            for i in range(index, lnums):
                if nums[i]>nums[index-1]:
                    self.swap(nums,index-1, i)
                    break
        

nums=[1,2,5,4,4,3,2,1,0]
sol=Solution()
sol.nextPermutation(nums)
print(nums)







