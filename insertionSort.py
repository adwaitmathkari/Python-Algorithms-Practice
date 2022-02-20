


# sorting
# sorting

# insertion sort
#  

l=[1, 12,1,1234,3,4,5,1,2,3,1,2,3,1,2,3,1,2,3, 2, 8, 6, -1, 7, 10, 14, 2, 1, 3, 1]

def insertionSort(l):
    # swapping
    #  
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j]<l[j-1]:
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp
            else: 
                break
    return l

print(insertionSort(l))






