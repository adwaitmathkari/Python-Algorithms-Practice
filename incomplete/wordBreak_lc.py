
"""

Given a non-empty string s and a dictionary wordDict containing a 
list of non-empty words, determine if s can be segmented into a space-separated
 sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""



# so now i will let that be for a while atleast
# and focus on the job at hand right now
# it is to solve this problem
#  

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DFS
        # start matching from the first index,
        # if a match is found, go to the next letter and match
        # if this word does not match, go to the next word to match, complete the wordDict
        # i can implement binary search on a sorted array
        # recursive algorithm?
        # like wordbreak('abcd', l):
        #           if ab matches
        #               wordbreak('cd', l)
        #           else:
        #               carry on to the next word in l
        #
        ans=[False]
        self.wordBreakRecur(s,wordDict,ans)
        return ans[0]
        


    def wordBreakRecur(self,s,l, ans):
        # print(s)

        if s=="":
            # print('anseqtrue')
            ans[0] = True
        for w in l:
            if ans[0]:
                # print(w,'ifansbreak')
                break
            if self.startsWith(s,w):
                self.wordBreakRecur(s[len(w):], l, ans)
    


    def startsWith(self,s,w):
        ln=len(w)
        if len(s)<ln:
            return False
        if s[0:ln] == w:
            return True
        return False 

wordDict = ["cats", "dog", "sand", "and", "cat","c", "ab"]
# print(sorted(wordDict))
s=Solution()
# print(s.startsWith('abc', 'abccc'))


ans=s.wordBreak('cabcabcabcabdogsandcatcabcababsandcats', wordDict)
print(ans)
print(s.wordBreak('acdfrcab', wordDict))

print(s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))







