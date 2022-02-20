"""
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        
        # 10th for 1234
        # 1 234 x6, 21 x2, 2314, 2341 
        # 10-1//6 = 1, (10-1%6)//2 = 1, 
       return ""