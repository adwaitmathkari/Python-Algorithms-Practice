

"""
You are given two strings S and T of the same length N . Your task is to convert the string S into T by doing some operations. 
In an operation, you can delete the first character of the string S and append any character at the end of the string. 
You are required to determine the minimum number of operations to convert S into T.


"""
def longestCommonSuffix(ln,s1,s2):
    for i in range(ln):
        if s1[i:]==s2[:ln-i]:
            return i
    return ln


ln= int(input())
s1=input()
s2=input()


print(longestCommonSuffix(ln,s1,s2))