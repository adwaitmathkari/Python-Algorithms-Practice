
def swap(l, i1,i2):
    temp=l[i1]
    l[i1]=l[i2]
    l[i2]=temp
 
 
def troubleSort(l):
    done=False
    iter1=0
    while(not done):
        iter1+=1
        done=True
        for i in range(len(l)-2):
            if l[i]>l[i+2]:
                swap(l,i,i+2)
                done=False
    print("iterations", iter1)
    return l

# l1=[6,5,4,3,2,1]
# l2=[1,2,5,8,3,4,9,6,7,10]
# print(troubleSort(l1))
# print(troubleSort(l2))


def troubleSortCorrect(l):
    """ prints OK if troubleSort sorts the list otherwise the index of first consecutive descending elements"""
    n=len(l)
    l1= [l[i] for i in range(0,n,2)]
    l2= [l[i] for i in range(1,n,2)]
    n1=len(l1)
    n2=n-n1
    l1.sort()
    l2.sort()
    for i in range(n1-1):
        if l1[i]>l2[i]:
            return 2*i
        elif l2[i]>l1[i+1]:
            return 2*i+1
    if(n1==n2):
        if l1[n1-1]>l2[n2-1]:
            return 2*(n1-1)
    return -1


t=int(input())
for x in range(1,t+1):    
    n=int(input())
    l=list(map(int, input().split()))
#     print(troubleSort(l))
    trouble = troubleSortCorrect(l)
    if trouble==-1:
        print("Case #%d: OK"%x)
    else:
        print("Case #%d: %d"%(x,trouble))
        

        
    
        
    
    
    
    
    
    
    
    

    
    