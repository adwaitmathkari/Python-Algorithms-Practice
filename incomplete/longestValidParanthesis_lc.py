"""
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) 
parentheses substring.
"""


class Solution:

    #brute force check from each ele which is longest length valid paranthesis
    def longestValidParentheses2(self, s: str) -> int:

        def longestStartingFrom(s, i):
            count = 0
            lastBestCount = 0
            b = 0
            for j in range(i, len(s)):
                if s[j] == "(":
                    b += 1
                else:
                    b -= 1
                if b < 0:
                    break
                count += 1
                if b == 0:
                    lastBestCount = count

            return lastBestCount

        maxln = 0
        for i in range(len(s)):
            ln = longestStartingFrom(s, i)
            if ln > maxln:
                maxln = ln
        return maxln

    # approach 2
    #
    def longestValidParentheses(self, s: str) -> int:
        pass
        