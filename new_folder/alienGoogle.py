
def swap(s,ind):
    s2=""
    for i in range(len(s)):
        if i==ind:
            s2+=s[ind+1]
            continue
        if i==ind+1:
            s2+=s[ind]
            continue
        s2+=s[i]
    return s2

def findLastC(s):
    """finds and returns the index of the last C which has an S after it"""
    sfound=False
    endCCount=0
    for i in range(len(s)-1,-1,-1):        
        if s[i]=="S":
            sfound=True 
        elif s[i]=="C":            
            if(sfound):            
                return (i,endCCount)
            endCCount+=1
    return (-1, endCCount)

# def deleteEndingCs(s):
#     sfound=False
#     index=len(s)
#     for i in range(len(s)-1, -1, -1):
#         if s[i]=="S":
#             sfound=True
#             break
#         elif(not sfound):
#             index=i
#     return s[:index]


t=int(input())
for x in range(1, t+1):
    d,sequence=input().split()
#     sequence= deleteEndingCs(sequence)        
    targetDamage=int(d)
    power=1
    nc,ns=0,0
    damage=0
    
    for ch in sequence:
        if(ch=="C"):
            power*=2
            nc+=1
        else:
            damage+=power
            ns+=1
#     print("damage", damage)
    hacks=0
    caseDone=False
    while(damage>targetDamage):
        lastC, endingCs=findLastC(sequence)
#         print("lastC",lastC)
        if(lastC==-1):
            print("Case #%d: IMPOSSIBLE"%x)
            caseDone=True
            break
        else:
            sequence=swap(sequence, lastC)
            damage-=(2**(nc-endingCs) - 2**(nc-endingCs-1))
#             print(sequence, damage)
            hacks+=1
    if not caseDone:
        print("Case #%d: %d"%(x,hacks))  
            
        
print("""Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 2
Case #5: 0
Case #6: 5
""")    
    
    


