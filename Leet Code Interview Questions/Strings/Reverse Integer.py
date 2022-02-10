"""
Here is my solution to the Reverse Integer Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
"""

class Solution:
    def reverse(self, x: int) -> int:
        y = None
        if x < 0:
            pointer1 = 1
            pointer2 = len(str(x)) - 1
        else:
            pointer1 = 0
            pointer2 = len(str(x)) - 1
        x = list(str(x))
        while pointer1 < pointer2:
            x[pointer1], x[pointer2] = x[pointer2], x[pointer1]
            pointer1 += 1
            pointer2 -= 1
            
        str1 = ""
        str1 = str1.join(x)
        print(str1, 'str1')
        print(type(str1))
        x = int(str1)
        if x < (- (2 ** 31)) or x > ((2 ** 31) - 1):
            return 0
        return x   
            
            