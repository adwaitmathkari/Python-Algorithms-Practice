


''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n = int(input())
    if(n==0):
        print(0)
        return 0
    l = []
    for i in range(n):
        l.append(int(input()))
    steps = sol(l,n)
    print(steps)
    return steps
    
def sol(l, n = 0):
    n = len(l)
    
    match = n
    matched=0
    for i in range(n-1, -1, -1):
        if l[i] == match:
            match-=1
            matched+=1
    print(n-matched)
    return n-matched

# main()


# # Write code here 

# print(main())

sol([4,1,2,5,3], 5)
sol([1],1)
sol([5,2,6,7,1,3,4], 7)
