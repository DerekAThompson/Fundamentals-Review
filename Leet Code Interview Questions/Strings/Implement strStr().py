"""
Here is my solution to the Implement strStr() Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) == len(haystack):
            if haystack == needle:
                return 0
            else:
                return -1
        for i in range(len(haystack)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1