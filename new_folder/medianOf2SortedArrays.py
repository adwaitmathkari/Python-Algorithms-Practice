#the median value is the middle value or the average of two middle values
#if there are 25 elements then 12 1 12
#26 elements: 12 1 1 12 
#thus take the mean of middle 2
#thus find ele with m+n-1//2 eles smaller
#strategy
#let se=(m+n-1)//2
#jump to se/2 in the first array
#go to se/2 in the second array
#see which is smaller
#if e1 is smaller then that means there are more than se smaller elements than e2 thus look at the halfway line in array 2
#other wise halfway in array1
# if there is no element in the smaller array then jump to higher place in array 1
#


class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        #define m+n-1 //2
        #se for smaller elements
        
        m=len(nums1)
        n=len(nums2)
        se=(m+n-1)//2
        
        #now to binary searching the element
        #final condition is :
        # find k s.t. nums1[k]>nums2[se-k-1] and nums1[k]<nums2[se-k]
        #this would mean that k nos less than nums1[k] in nums1 
        #           and exactly se-k nos smaller than nums1[k] in nums2
        #           thus total se nos smaller than nums1[k]
        #if m+n is odd return nums1[k] else find the next smallest no and return their mean
        
        #setting up the recursion
        
        
        
        
        
        
        