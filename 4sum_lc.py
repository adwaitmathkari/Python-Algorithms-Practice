"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.


"""

from typing import List
import time


## O(n^4) time complexity
class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        set1 =set()
        nums= sorted(nums)
        ln=len(nums)
        sum1=0
        for i in range(ln-3):
            # print('i=',i)
            sum1=nums[i]
            for j in range(i+1,ln-2):
                sum1 = nums[i]+nums[j]

                for k in range(j+1,ln-1):
                    sum1=nums[i]+nums[j]+nums[k]

                    for l in range(k+1, ln):
                        sum1=nums[i]+nums[j]+nums[k]+nums[l]
                        if sum1==target:
                            set1.add((nums[i], nums[j], nums[k], nums[l]))

        final = [list(tup) for tup in list(set1)]
        return final

                    

    



## O(n^2) time complexity
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        finalSet = set()
        # nums= sorted(nums)

        # overall: find pairwise sums, 
        # add all pair sums in a dictionary and a list
        # in the dictionary add the sum as key and as value a list of pairs that have the sum. 
        # check whether the needed sum is there in the dictionary
        # finally add legal pairs according to whether there are any repetitions and whether the repeated no exists in the list that no of times.
        # ;aslkdj;slakdf;lkas;lksjad;lfjs;adlkfj;sdlaf


        occurenceDict = {}
        for num in nums:
            occurenceDict[num] = occurenceDict.get(num,0)+1
            # dictionary.get() function return the value if key exists and the 
            # second parameter is returned if the key does not exist
            
            # if num in occurenceDict.keys():
            #     occurenceDict[num]+=1
            # else:
            #     occurenceDict[num]=1
        
        lnums=len(nums)

        # 2 sum dict
        pairSumDict = {}
        for i in range(lnums-1):
            for j in range(i,lnums):
                pairSum = nums[i]+nums[j]

                # here the sum pairs are stored as a list and it is easy to iterate over it 
                l= pairSumDict.get(pairSum, [])
                if (nums[i], nums[j]) not in l:
                    l+= [(nums[i], nums[j])]
                pairSumDict[pairSum] = l
                

                # here the sum pairs are stored in a set and thus there are no 
                # try:
                #     s = pairSumDict[pairSum]
                #     s.add((nums[i], nums[j]))
                #     pairSumDict[pairSum] = s
                # except(KeyError):
                #     s=set()
                #     s.add((nums[i], nums[j]))
                #     pairSumDict[pairSum] = s

        # sol
        for i in range(lnums-1):
            for j in range(lnums):
                n1 = nums[i]
                n2 = nums[j]
                neededSum = target - n1 - n2
                if neededSum in pairSumDict:
                    for otherPair in pairSumDict[neededSum]:
                        n3=otherPair[0]
                        n4=otherPair[1]

                        #check whether any equality is there and whether that no exists in nums more than once
                        d = {}
                        for n in [n1, n2, n3, n4]:
                            d[n] = occurenceDict[n]
                        
                        add = True
                        for n in [n1, n2, n3, n4]:
                            if d[n] == 0:
                                add = False
                            d[n]-=1
                        if add:
                            finalSet.add(tuple(sorted([n1,n2,n3,n4])))
        
        # final = [list(tup) for tup in list(finalSet)]
        # return final
        return(list(map(list,finalSet)))



#Used to easily generate combinations
import itertools

#picked up from leetcode
class Solution3:

    #Helper function to create a frequency count of a list of numbers
    def count(self, nums):
        result = {}

        for value in nums:
            result[value] = result.get(value, 0) + 1

        return result
		
    #for a given solution do we have enough numbers to fulfill that solution?
    def is_valid(self, solution, nums):
        sol_freq = self.count(solution)

        for key in sol_freq:
            if sol_freq[key] > nums.get(key, 0):
                return False

        return True

    def fourSum(self, nums, target):
        result = set()
		
	    #Later I will generate all possible answers and use this number frequency table to rule out answers that need more numbers than we have.
        num_freq = self.count(nums)

        #sums is going to store a map of all pairs of numbers where the key is their sum
        sums = {}

        #Iterate through all 2-element combinations of numbers and store them in sums by their sum.
        for pair in itertools.combinations(nums, 2):
            s = sum(pair)
            sums[s] = sums.get(s, []) + [pair]

        #Iterate through the keys, representing all unique sums of all 2-element pairs, find a matching "conjugate" that sums with the key to target.
        for key in sums:
            conjugate = target - key

            if conjugate in sums:
                for ans in map(lambda x: x[0] + x[1], itertools.product(sums[key], sums[conjugate])):
				    #Storing each result as a sorted tuple in a set prevents duplicates.
                    result.add(tuple(sorted(ans)))

        #remove from the list of results any possible solutions which we don't have enough numbers to actually fulfill.
        result = filter(lambda x: self.is_valid(x, num_freq), result)

        #change the elements in result so that they are a list of lists instead of a set of tuples.
        return list(map(list, result))




from collections import Counter
## much faster solution according to leetcode
## turns out this is an optimized O(n^3) solution and this wont exactly give fast 
## results if target is high and the nos are all close to each other 

class Solution4:
    '''
    Fibonacci sequence is the answer, because A[n] = A[n-1] + A[n-2]
    '''

    def four_sum_wip(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4:
            return []
        ans = []
        nums.sort()
        ccn = Counter(nums)
        if ccn[0] > 3:
            ans.append([0,0,0,0])
        pos_set = set([x for x in nums if x > 0])
        neg_set = set([x for x in nums if x < 0])

        return ans

    def four_sum_jmansuri(self, n: List[int], t: int) -> List[List[int]]:
        '''
        Runtime: 56 ms, faster than 99.20% of Python3 online submissions for 4Sum.
        Memory Usage: 14 MB, less than 7.14% of Python3 online submissions for 4Sum.
        - Junaid Mansuri
        # (LeetCode ID)@hotmail.com
        '''
        if not n:
            return []
        n.sort()
        L, N, S, M = len(n), {j:i for i,j in enumerate(n)}, set(), n[-1]
        for i in range(L-3):
            a = n[i]
            if a + 3*M < t: continue
            if 4*a > t: break
            for j in range(i+1,L-2):
                b = n[j]
                if a + b + 2*M < t:
                    continue
                if a + 3*b > t:
                    break
                for k in range(j+1,L-1):
                    c = n[k]
                    d = t-(a+b+c)
                    if d > M:
                        continue
                    if d < c:
                        break
                    if d in N and N[d] > k:
                        S.add((a,b,c,d))
        return S

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.four_sum_jmansuri(nums, target)


l12=[2500,2500,2500,2500,10000,0,0,0,5000,4000,6000,8000,5000,2000,2000,1000,1000,3000,3000,7000,2500,2500,2500,2500,10000,0,0,0,5000,4000,6000,8000,5000,2000,2000,1000,1000,3000,3000,7000,2500,2500,2500,2500,10000,0,0,0,5000,4000,6000,8000,5000,2000,2000,1000,1000,3000,3000,7000,2500,2500,2500,2500,10000,0,0,0,5000,4000,6000,8000,5000,2000,2000,1000,1000,3000,3000,7000,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481,2500,2500,2500,2500,10000,0,0,0,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481]
tar12=10000

# l12=[-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481,2500,2500,2500,2500,10000,0,0,0,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481,-497,-481,-481,-472,-471,-465,-422,-420,-413,-405,-388,-381,-366,-361,-359,-348,-334,-334,-318,-310,-305,-280,-273,-272,-262,-254,-248,-223,-208,-202,-196,-192,-189,-167,-165,-165,-156,-143,-136,-122,-120,-120,-108,-77,-50,-44,-34,-26,-17,-5,13,46,46,53,54,56,66,71,72,75,89,115,130,139,149,151,154,196,209,219,230,240,245,246,253,267,277,289,299,302,303,304,342,349,360,361,361,375,392,400,407,408,408,426,427,429,443,451,481]
# tar12=2000


s1=Solution3()
print(s1.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s1.fourSum([1,-2,-5,-4,-3,3,3,5],-11))
t=time.time()           
print(len(s1.fourSum(l12,tar12)))
print( time.time()-t)





s1=Solution()
print(s1.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s1.fourSum([1,-2,-5,-4,-3,3,3,5],-11))
t=time.time()   
print(len(s1.fourSum(l12,tar12)))
print( time.time()-t)




s1=Solution4()
print(s1.fourSum([1, 0, -1, 0, -2, 2], 0))
print(s1.fourSum([1,-2,-5,-4,-3,3,3,5],-11))
t=time.time()     
print(len(s1.fourSum(l12,tar12)))
print(time.time()-t)

