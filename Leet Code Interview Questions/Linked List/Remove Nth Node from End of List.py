"""
Here is my solution to the Remove Nth Node From End of List Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        node1 = head
        node2 = head
        while node1.next:
            if count != (n + 1):
                count += 1
                node1 = node1.next
            elif count == (n + 1):
                node1 = node1.next
                node2 = node2.next
        if count == n:
            return node2.next
        node2.next = node2.next.next
        return head
            