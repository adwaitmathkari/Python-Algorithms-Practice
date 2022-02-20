import random
l=[0,0,0]
s=0
n=1000000
for i in range(n):
    l[0] = random.randint(0, 5)
    l[1] = random.randint(0, 5)
    l[2] = random.randint(0, 5)
    if (0 in l):
        s+=1

print(s/n)