"""
Here is my solution to the String to Integer (atoi) Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        print(s,'no strip')
        s = s.lstrip()
        print(s,'stripped')
        s = list(s)
        if len(s) == 0:
            return 0
        start = 0
        newString =""
        flag = 0
        if s[0] == '-':
            flag = 1
            start = 1
        elif s[0] == '+':
            flag = 0
            start = 1
        for i in range(start, len(s)):
            if s[i].isdigit():
                print(s[i], i)
                newString += s[i]
                print(s[i], newString)
            else:
                break
        print(newString)
        if len(newString) == 0:
            s =0
        else:
            s = int(float(newString))
        print(s, 's', type(s))
        if flag == 1:
            s = -(s)
        if (-(2 ** 31)) < s:
            if s < ((2 ** 31) - 1):
                return s
            else:
                return ((2 ** 31) - 1)
        else:
            return (-(2 ** 31))
        