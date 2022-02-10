"""
Here is my solution to the Linked List Cycle Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        if head.next.next == head:
            return True
        node1 = head
        node2 = head
        while node2.next is not None and node2.next.next is not None:
            node1 = node1.next
            node2 = node2.next.next
            print('here')
            if node1 is node2:
                return True
        return False