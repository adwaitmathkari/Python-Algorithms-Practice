
# Complete the powerSum function below.


def ps(x, n, added, lastAdded):
    if x<0:
        return 0
    if x==0:
        print(added)
        return 1 

    sols = 0

    for i in range(lastAdded+1, 33):        
        if i**n > x:
            break
        if i not in added:
            sols += ps(x-i**n, n, added[:]+[i], i)
    
    return sols

print(ps(1000, 2, [], 0))
