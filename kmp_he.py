'''

Given 2 strings, P and T, find the number of occurrences of P in T.

Input:

First line contains string P, and second line contains the string T.

Output:

Print a single integer, the number of occurrences of P in T.

Constraints: 1<P<=T10^5

'''



p=input()
s=input()

# kmp
# make the array
def makeLPSArray(p):
    l=[]
    def lps(p):
        ln=len(p)
        longestLength=0
        for i in range(ln-1):
            k=ln-i-1
            if p[:i+1]==p[k:]:
                longestLength=i+1
    
        return longestLength

    for i in range(len(p)):
        l.append(lps(p[:i+1]))
    return l




print(makeLPSArray(p))


