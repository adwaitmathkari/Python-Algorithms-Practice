class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        else:
            s=self.countAndSay(n-1)
            
            count = 1
            retS=''
            for i in range(1,len(s)):
                if s[i]!=s[i-1]:
                    retS+=str(count)+s[i-1]
                    count=1
                else:
                    count+=1
            retS+=str(count)+s[len(s)-1]
            return retS


s=Solution()
for i in range(4):
    k=int(input())
    print(s.countAndSay(k))
