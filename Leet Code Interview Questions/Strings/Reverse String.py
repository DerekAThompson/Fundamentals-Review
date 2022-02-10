"""
Here is my solution to the Reverse String Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer1 = 0
        pointer2 = len(s) - 1
        
        while pointer1 < pointer2:
            s[pointer1], s[pointer2] = s[pointer2], s[pointer1]
            pointer1 += 1
            pointer2 -= 1
        pass 