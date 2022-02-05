"""
Here is my solution to the Linked List Cycle Problem on Leet Code
https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        twoStep = head
        oneStep = head
        while twoStep.next is not None and twoStep.next.next is not None:
            twoStep = twoStep.next.next
            oneStep = oneStep.next
            if twoStep is oneStep:
                return True
        return False