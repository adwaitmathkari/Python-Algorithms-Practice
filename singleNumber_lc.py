"""Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?"""


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            try:
                del d[i]
            except KeyError:
                d[i] = 1
        for k in d.keys():
            return k




s=Solution()
print(s.singleNumber([1,2,3,4,5,2,4,5,1,7,7,8,9,9,8]))





