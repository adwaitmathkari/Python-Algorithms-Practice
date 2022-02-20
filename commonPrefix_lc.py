class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[1]
        if strs==[]:
            return ''
        
        l1=len(strs[0])
        in1=0
        l2=len(strs[1])
        in2=1
        
        for i in range(len(strs)):
            ln=len(strs[i])
            if ln < l2:
                if ln <l1:
                    l2=l1
                    in2=in1
                    l1=ln
                    in1=i
                else:
                    l2=ln
                    in2=i
        
        s1=strs[in1]
        s2=strs[in2]
        commonString = ''
        for i in range(l1):
            if s1[i]==s2[i]:
                commonString += s1[i]
            else: 
                break
        for i in range(len(strs)):
            cs2=''
            
            for j in range(len(commonString)):
                if strs[i][j]==commonString[j]:
                    cs2+=commonString[j]
                else:
                    break
            commonString = cs2
            
        return commonString


s=Solution()

l= ['needle', 'needless', 'needful']
print(s.longestCommonPrefix(l))