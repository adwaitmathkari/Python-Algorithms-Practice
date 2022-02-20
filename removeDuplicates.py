from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            temp = nums[i]
            if nums[i] != prev:
                self.swap(nums, p, i)
                p+=1
            prev = temp
        return p

    
    def swap(self, l, i1, i2):
        temp=l[i2]
        l[i2]=l[i1]
        l[i1]=temp


s = Solution()
a = [1,2,3,4,5,5,5,6,6,6,7,8,10,10,10,101]
a=[1,2,3,4,5,6,7,8,9]
print(a[0:s.removeDuplicates(a)])
# print(a)
