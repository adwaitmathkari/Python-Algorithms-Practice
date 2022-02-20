from typing import List

def subarraySumZero(n, arr):
    # sum of arr[i,j] = sum(arr[0,j]) - sum(arr[0,i])
    # so hash the sums 0,i for i  in 0-n
    # and now, for each sum(0,i) if there exists sum(0,i) - sum(0,j) = 0 then return true

    #go on hashing 0,i as I go on 0-n otherwise, hash(0,i)==hash(0,i) will always be there in the set

    # so
    sum1 = 0
    set1 = set()
    set1.add(0)
    n= len(arr)
    for i in range(0, n):
        sum1 = sum1 + arr[i]

        #set will have sums of 0,j for all j less than i
        #thus if we have sum1 in set for any j less than i that means that there is an array whose sum will be 0
        #what if this sum1 itself is zero-- added a zero in the set so that that owuld be for sum of zero array
        #elements and that will give the subarray that starts from element 1

        if sum1 in set1:
            return True
    
        #after checking, add sum1 to the array for the next elements
        set1.add(sum1)

    return False


def subarraySum(self, nums: List[int], k: int) -> int:
    sum1 = 0
    set1 = set()
    set1.add(0)
    n= len(arr)
    count = 0
    for i in range(0, n):
        sum1 = sum1 + arr[i]

        #set will have sums of 0,j for all j less than i
        #thus if we have sum1 in set for any j less than i that means that there is an array whose sum will be 0
        #what if this sum1 itself is zero-- added a zero in the set so that that owuld be for sum of zero array
        #elements and that will give the subarray that starts from element 1

        if sum1-k in set1:
            count+=1
    
        #after checking, add sum1 to the array for the next elements
        set1.add(sum1)

    return count

def firstUniqueInteger(lis):
    d={}
    for i in lis:
        d[i] = d.get(i,0)+1
    for k in d.keys():
        if d[k]==1:
            return k
    return -1


arr1 = [[],[4,3,2,7,8,-3,-12], [1,2,1,2], [1,1], [0], [0,0,5,6,6,1,9,10,10], [1,-1], [1,2,3], [1,2,3,-6]]
for arr in arr1:    
    print(firstUniqueInteger(arr))
