"""
Here is my solution for the Reverse Linked List Problem
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        global count
        global maxCount
        if not head:
            return
        elif head:
            count = 1
        counter(head)
        maxCount = count
        count = 0
        return flipLinkedList(head)

def counter(node):
    global count
    if node.next:
        count += 1
        counter(node.next)
    pass
        
def flipLinkedList(node):
    global count
    global maxCount
    global head
    count += 1
    if count == maxCount:
        head = node
    if node.next:
        flipLinkedList(node.next)
        node.next.next = node
        count -= 1
    if count == 1:
        node.next = None
    return head