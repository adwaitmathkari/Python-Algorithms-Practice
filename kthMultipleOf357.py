def kthMultiple(k):
    l=[]
    # find all the 100 powers of 5,7,3 
    # (3,5,7) ** 0-9,
    for i in range(25):
        for j in range(25):
            for k1 in range(25):
                l.append(3**i * 5**j * 7**k1)
    l.sort()
    print(len(l))
    return l[k-1]

print(kthMultiple(323))

# for i in range(15):
    # print(3**i, 5**i, 7**i)