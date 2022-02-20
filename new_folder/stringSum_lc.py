"""Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
# "178290405701247"
# "1235712862"
#  ans= "...4109"  



class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1=len(num1)
        l2=len(num2)
        l=max(l1,l2)
        
        answer = ""
        carried=0
        for i in range(1,l+1):
            if i<=l1:
                carried+=int(num1[-i])
            if i<=l2:
                carried+=int(num2[-i])
            
            strCarried = str(carried)
            if carried>9:
                carried=int(strCarried[0])
                answer = strCarried[1]+answer
            else:
                carried=0
                answer = strCarried+answer
        if carried!=0:
            answer = str(carried)+answer
        print(answer)
        return answer



s=Solution()
s.addStrings("1","9999999")

