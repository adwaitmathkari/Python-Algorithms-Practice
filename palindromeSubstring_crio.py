# Given a string s, partition s into substrings such that substring is a palindrome.
# Return all possible palindrome partitioning of s.
# Input format
# The string s
# Output format
# On each new line, print a different way of partitioning the string into substrings that are palindromes.
# Constraints
# 0 <= |s| <= 18

# Sample Input 1
# aabc
# Sample Output 1
# aa b c
# a a b c



# so to do this problem..
# dp is very good here 
def palindromePartitioning(s):
    finalList = []
    palPartitions(s, [], finalList)
    return finalList



def ispal(s):
        if len(s)==0 or len(s)==1:
            return True
        else:
            return s[0]==s[-1] and ispal(s[1:-1])


def palPartitions(s, partitions, finalList):
    if s=='':
        finalList.append(partitions)
        
    for i in range(len(s)):
        if ispal(s[:i+1]):
            partitions1 = partitions[:]
            partitions1.append(s[:i+1])
            palPartitions(s[i+1:], partitions1, finalList)


print(palindromePartitioning('aabcac'))