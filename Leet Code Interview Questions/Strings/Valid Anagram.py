"""
Here is my solution to the Valid Anagram Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}
        for i in range(len(s)):
            charDict[s[i]] = charDict.get(s[i], 0) + 1
        print('charDict', charDict)
        for j in range(len(t)):
            try:
                charDict[t[j]] -= 1
            except:
                return False
        print(charDict, 'part 2')
        if all(values == 0 for values in charDict.values()):
            return True
        print('anywhere')
        return False