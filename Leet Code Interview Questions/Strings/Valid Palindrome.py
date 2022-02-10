"""
Here is my solution to the Valid Palindrome Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.strip()
        s = s.lower()
        alFilter = filter(str.isalnum, s)
        s = "".join(alFilter)
        pointer1 = 0
        pointer2 = len(s) - 1
        while pointer1 < pointer2:
            if s[pointer1] == s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
                continue
            else:
                return False
        return True