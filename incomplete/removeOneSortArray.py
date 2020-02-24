"""
Given an array sort remove one element so that it gets sorted in ascending order. 

Return -1 if it is not possible.

"""

class Solution:
    @staticmethod
    def removeSort(l):
        for i in range(len(l)):
            