def search(nums, target):
    # Your implementation goes here
    return binary(nums,target, 0,len(nums)-1)



def binary(n,t, left, right):    
    mid = (left+right )//2
    
    if left>right:
        return -1
    if t == n[mid]:
        return mid
    
    m = n[mid]
    l = n[left]
    r = n[right]
    
    if m>=l:
        if t<m and t>=l:
            return binary(n, t, left, mid-1)
        else:
            return binary(n,t,mid+1, right)
    else:
        if t>m and t<=r:
            return binary(n,t, mid+1, right)
        else:
            return binary(n,t, left, mid-1)
    


nums = [8,9,10,11,12,13,1,2,3,4,5]
indices = [14,8,9,10,11,12,13,14,1,2,3,4,5,6,7]
# nums = [6,4]
# indices = [6,4,11,3]

for i in indices:
    print((str(i)+'   ')[:4], ('  ' + str(search(nums, i)))[-3:])
    
    