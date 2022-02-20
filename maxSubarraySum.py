class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        sum1=0
        l=[]
        
        for i in range(n):
            sum1 += nums[i]
            l.append(sum1)
        
        minsum = 0
        l1=[]
        for i in range(n):
            l1.append(l[i] - minsum)
            minsum = min(minsum, l[i])
        
        return max(l1)


    #kadane's algorithm
    def maxSubArray1(self, nums: List[int]) -> int:        
        c1=c2=nums[0]
        for i in range(1, len(nums)):
            c2=c2+nums[i] if c2>0 else nums[i]
            c1=max(c1,c2)
        return c1