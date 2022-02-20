"""
Given an array sort remove one element so that it gets sorted in ascending order. 

Return -1 if it is not possible.

"""
# 1 2 3 4 8 3 9 17
# 1 2 3 1 5 6 7 9



import random
class Solution:

    @staticmethod
    def removeSort(l):
        for i in range(len(l)-1):
            if l[i+1]<l[i]:
                if i==0:
                    del(l[i])
                    break
                elif l[i+1]>=l[i-1]:
                    del l[i]
                    break
                else:
                    del l[i+1]
                    break
        return l



l1=[1,2,3,4,5,3,9,17]
l2=[1,2,3,4,17,8,9,10]
l3=[1,2,3,4,5,6,7,8,1]
l4=[10,1,2,3,4]
l5=[1,10,2,3]

l=[l1,l2,l3,l4,l5]
for li in l:
    print(Solution.removeSort(li))



badSol=0
l=[i for i in range(1000,2000)]
for a in range(10000):
    r1 = random.randint(0,100)
    r2 = random.randint(0,3000)
    l1=l[:]
    l1.insert(r1,r2)
    l1=Solution.removeSort(l1)

    # for i in range(len(l1)-1):
    #     if l1[i+1]<l1[i]:
    #         badSol+=1
    #         break
    

    if sorted(l1)!=l1:
        badSol+=1



print(badSol)

l12=[12, 12,123,12,123,123,123,1233,3,2,3,1,4,1,1230]
print(sorted(l12)==l12)