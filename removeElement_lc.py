from typing import List

"""Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length."""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #will swap the elements to the end of the array.
        #two indices i at the start, j at the end
        #increment i if is not ele
        #decrement j if j is ele
        
        
        i=0
        j=len(nums)-1
        
        while i<=j:
            if nums[i]==val and nums[j]!=val:
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            elif nums[i]!=val:
                i+=1
            elif nums[j]==val:
                j-=1
        print(j)
        
s=Solution()
nums=[1,2,3,2,3,4,3,5,3,4,5,5,567,567,42,5234,64,8568,3,4,5,6,7]
s.removeElement(nums,3)
print(nums)       
        