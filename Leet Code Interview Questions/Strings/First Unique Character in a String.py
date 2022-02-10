"""
Here is my solution to the First Unique Character in a String Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrenceDict = {}
        s = list(s)
        print(s)
        for i in range(len(s)):
            occurrenceDict[s[i]] = occurrenceDict.get(s[i], 0) + 1
        for i in range(len(s)):
            if occurrenceDict.get(s[i]) == 1:
                return i
        return - 1