#python
t=int(input())

print(t)
for i in range(t):
    index = 0
    n=int(input())
    while True:
        if 2**index > n+1:
            print(2**(index-1)-1)
            break
        index+=1

# 1,10,11,100,101,110,111, 1000
