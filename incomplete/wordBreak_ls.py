
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
        
        pass


wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sorted(wordDict))
