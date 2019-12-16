class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ln=len(nums)
        set1=set()
        set2=set()
        nums1=nums
                
        #add the nums to set and if a no is repeated then add it to repeated nums set
        for i in range(ln):
            if nums[i] in set1:
                set2.add(nums[i])
            else:
                set1.add(nums[i])
                
        
        #to better the sol, 
        #optimize nums to keep only 2 entries of repeated nos
        #as 3 nums can be only 0+0+0 any other will be positive or negative
        nums=list(set1)+list(set2)
        ln=len(nums)
        
        
        # check each pair once o(n square)
        # if the resulting sum is equal to one of the nos then need to check in the 
        # repeated nos set(set2)
        # nums1.sort()
        
        finalSet=set()
        for i in range(ln):
            for j in range(i+1, ln):
                
                #thus here we have a pair of nos at i and j in nums
                sum1 = nums[i]+nums[j]
                if -sum1 != nums[i] and -sum1!=nums[j] :
                    if -sum1 in set1:
                        l1=[nums[i],nums[j], -sum1]
                        finalSet.add(tuple(sorted(l1)))
                elif -sum1 in set2:
                    l1=[nums[i],nums[j], -sum1]
                    finalSet.add(tuple(sorted(l1)))
        
        if (0,0,0) in finalSet:
            zeroes=0
            for i in range(len(nums1)):
                if nums1[i]==0:
                    zeroes+=1
            if zeroes<3:
                finalSet.remove((0,0,0))

        finalList=list(finalSet)
        
        for i in range(len(finalList)):
            finalList[i]=list(finalList[i])
            
        return finalList
    
    
    
    
        








