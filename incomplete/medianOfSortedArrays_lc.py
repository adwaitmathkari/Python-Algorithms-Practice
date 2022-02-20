"""

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

"""
from typing import List

l1 = [1, 1, 3, 5, 7, 9, 21, 120, 120, 122, 139]
l2 = [2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 20, 20,
      20, 20, 22, 22, 22, 23, 24, 26, 27, 28, 219]

l1 = [1, 2, 4, 6, 8, 10]
l2 = [3, 6, 11, 14]


def median(l1, l2):
    assert l1 == sorted(l1)
    assert l2 == sorted(l2)
    l = sorted(l1+l2)
    ln = len(l)
    if ln % 2 == 0:
        return ((l[ln//2 - 1] + l[ln//2]) / 2)
    else:
        return (l[(ln-1)//2])


print(median(l1, l2))


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

    def findMedian(self, l1, l2, s, e, ans):
        # find k where exactly (nele-1)//2 elements are lesser than k
        nele = len(l1) + len(l2)
        #n of elements that should be less than the given no
        nless = nele-1
        nless = nless//2

        m = (s+e)//2
        # no of less than l1[m]
        if s > e:
            return
        # m smaller elements in nums1
        #thus nlesser - m elements need to be seen in nums2
        if nless-m < 0:
            self.findMedian(l1, l2, s, m-1, ans)
            return  
        if nless - m == 0:
            if l1[m]<l2[0]:
                return l1[m]
            else:
                self.findMedian(l1,l2,s,m-1, ans)
        
        if l2[nless - m ] >= l1[m] and l2[nless - m - 1] <= l1[m]:
            ans[0] = l1[m]
            return
        if l2[nless - m] < l1[m]:
            findMedian(l1,l2, s, m-1, ans)
            return
        
        if l2[nless-m] >= l1[m]:
            ans[0] = l1[m]
            return
