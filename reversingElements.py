arr1 = input().split(" ")
n = int(arr1[0])
q = int(arr1[1])

arr2 = input().split(" ")
for i in range(n):
    arr2[i] = int(arr2[i])


def reverse(arr, e1, e2):
    arr2 = arr.copy()
    for i in range(e1,e2+1):
        arr2[i] = arr[e1+e2-i]
    return arr2
    

for i in range(q):
    arr3 = input().split(" ")
    e1 = int(arr3[0])-1
    e2 = int(arr3[1])-1
    arrtemp = reverse(arr2, e1, e2)
    # print(arrtemp)
    start = -1
    pointer = 0
    s = 0
    finalSum = 0

    while(pointer < n):
        start+=1
        pointer = start 
        s=0
        while(s>=0):
            s+=arrtemp[pointer]
            pointer+=1
            if(s>finalSum):
                finalSum = s
                
            if(pointer == n):
                break
    print(finalSum)
    


