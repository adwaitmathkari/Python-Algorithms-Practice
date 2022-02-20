


import random
import time

def kUniqueSubstring(l, k):
    d={}
    pointer =-1
    maxLen =0 
    for i in range(len(l)):
        pointer+=1
        while True:
            if pointer == len(l):
                pointer -=1
                break
            dkeys = d.keys()
            if l[pointer] not in dkeys:
                if len(dkeys) == k:
                    pointer-=1
                    break
                d[l[pointer]] = 1
                pointer +=1
            else:
                d[l[pointer]] +=1
                pointer +=1
        
        maxLen = max(maxLen, pointer-i+1)
        d[l[i]] -=1
        if d[l[i]] == 0:
            del d[l[i]]
    
    return maxLen

#slow
def length_of_substring(s, k):
    # simple sol
    maxLen = 0

    for i in range(len(s)):
        set1 = set()
        uniqueEle = 0
        if len(s)-i < maxLen:
            break
        for j in range(i,len(s)):
            if s[j] not in set1:
                uniqueEle+=1
                if uniqueEle>k:
                    maxLen = max(maxLen, j-i)
                    break
                set1.add(s[j])
            if j == len(s)-1:
                maxLen = max(maxLen, j-i+1)
                return maxLen
    
    return maxLen

def main():

    fruitlists = [[],[1,2,1,2,3,4,3,7,7,3,7,7],[1,2,1,2,1,2], [1,2,3,4,5,6,7,8,9], [1,2,1], [1,2,3,4,3,4,3,4,3,5,6,7,8,4,5,6,5,7,5,8], [1]]
    testlist=''
    s='abcdefghijklmnopqrstuvwxyz'
    for i in range(100000):
        testlist+=s[random.randint(0,25)]
    
    t=time.time()
    print(kUniqueSubstring(testlist, 20))
    print(time.time()-t)
    print('XXXXXXXX')
    t=time.time()
    print(length_of_substring(testlist, 20))
    print(time.time()-t)

    print('XXXXXXXX')
    print(kUniqueSubstring('aabasdkjhsdakjfgaskdjfgabcdeabcdeabcde',5))
    
        


    # for fruits in fruitlists:
    #     print('XXXXXXXX')
    #     print(kUniqueSubstring(fruits, 2))

if __name__ == "__main__":
    main()
