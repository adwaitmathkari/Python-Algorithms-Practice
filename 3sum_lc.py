from typing import List

class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    n=len(nums)
    numsSet=set(nums)
    finalSet = set()
    for i in range(n-1):
      for j in range(i+1,n):
        sum_= -1*(nums[i]+nums[j])
        if sum_ in numsSet:
          l1=[nums[i], nums[j], sum_]
          l1.sort()
          s1=str(l1[0])+','+str(l1[1])+','+str(l1[2])
          finalSet.add(s1)   
    finalList = []
    for ele in finalSet:
      ele=ele.split(',')
      ele[1]=int(ele[1])
      ele[2]=int(ele[2])
      ele[0]=int(ele[0])
      finalList.append(ele)
    return finalList


sol = Solution()
nums=[1,0,-1,-2,-1,3]
print(sol.threeSum(nums))











