"""
Here is my solution to the Longest Common Prefix Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/887/
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1 = min(strs)
        str2 = max(strs)
        for i, char in enumerate(str1):
            if char != str2[i]:
                return str2[:i]
        return str1