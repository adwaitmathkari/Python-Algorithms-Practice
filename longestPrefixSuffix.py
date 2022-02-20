'''
Given a string of character, find the length of longest proper prefix which is also a proper suffix.
Example:
S = abab
lps is 2 because, ab.. is prefix and ..ab is also a suffix.

Input:
First line is T number of test cases. 1<=T<=100.
Each test case has one line denoting the string of length less than 100000.

Expected time compexity is O(N).

Output:
Print length of longest proper prefix which is also a proper suffix.

Example:
Input:
2
abab
aaaa

Output:
2
3

'''

t=int(input())


for _ in range(t):
    s=input()
    ln=len(s)
    longestLength=0
    for i in range(ln-1):
        k=ln-i-1
        if s[:i+1]==s[k:]:
            longestLength=i+1
    
    print(longestLength)
    
