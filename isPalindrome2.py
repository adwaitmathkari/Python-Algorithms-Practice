import string

class Solution:
#     def isPalindrome(self, s: str) -> bool:
        
#         ascii1 = string.ascii_letters + string.digits
#         s1=''
#         for ch in s:
#             if ch in ascii1:
#                 s1+=ch
        
#         for i in range(len(s1)//2):
#             if s1[i].lower()!=s1[len(s1)-i-1].lower():
#                 return False
#         return True
    
    def isPalindrome(self, s: str) -> bool:
        
        ascii1 = string.ascii_letters + string.digits
        
        i=0
        j=len(s)-1
        while i<j:
            if s[i] not in ascii1:
                i+=1
            elif s[j] not in ascii1:
                j-=1
            else:
                if s[i].lower()!=s[j].lower():
                    return False 
                else:
                    i+=1
                    j-=1
        
        return True  
             