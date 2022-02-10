"""
Here is my solution to the Palindrome Linked List Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
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