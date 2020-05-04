"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.


"""



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #1 make pairwise sums and hash them all
        pass

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        set1 ={}
        nums= sorted(nums)
        l=len(nums)
        
        sum1=0
        for i in range(l):
            sum1=nums[i]
            if sum1>target:
                continue
            for j in range(i+1,l):
                sum1 = nums[i]+nums[j]

                if sum1>target:
                    continue
                for k in range(j+1,l):
                    sum1=nums[i]+nums[j]+nums[k]
                    if sum1>target:
                        continue
                    
                    



        
    
        