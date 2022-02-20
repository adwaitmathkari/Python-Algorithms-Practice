
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    if len(scores) == 0:
        return [1 for i in range(len(alice))]
    
    scores1 = [scores[0]]
    aliceRanks = []
    for i in range(1,len(scores)):
        if scores[i] != scores[i-1]:
            scores1.append(scores[i])
    lscores1 = len(scores1)
    for a in alice:
        ind, found = binaryPos(scores1, a, 0, lscores1-1)
        if found:
            aliceRanks.append(ind+1)
        else:            
            if ind>=lscores1:
                ind=lscores1-1
            elif ind==-1:
                ind=0 
            if a<scores1[ind]:
                aliceRanks.append(ind+2)
            else:
                aliceRanks.append(ind+1)
    
    return aliceRanks
    

def binaryPos(arr, t, l, r):
    # print(l,r)
    m = (l+r)//2
    if l > r:
        return l, False
    if arr[m] == t:
        return m, True
    
    if t < arr[m]:
        return binaryPos(arr, t, m+1, r)
    else:
        return binaryPos(arr, t, l, m-1)
    

# scores=[10,9,9,8,8,8,6,5,5,5,3]
# alice = [9,2,0,7,6,11,10]
scores=[8,7,2,1]
alice = [9,2,0,7,6,11,10]
print(climbingLeaderboard(scores, alice))