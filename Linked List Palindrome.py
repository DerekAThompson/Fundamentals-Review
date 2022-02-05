"""
Here is my solution to the Palindrome Linked Problem on Leet Code
https://leetcode.com/problems/palindrome-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        checker = []
        while current:
            checker.append(current.val)
            current = current.next
        if checker == checker[::-1]:
            return True
        return False