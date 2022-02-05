"""
Here is my solution to the Delete the Middle Node of a Linked List Problem on Leet Code
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/submissions/
"""




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        returnList = []
        
        if not head:
            return returnList
        
        current = head
        count = 1
        
        # Generates the number of nodes of the Linked List
        while current:
            if current.next is head or current.next is None:
                break
            else:
                current = current.next
                count += 1
        
        # Finds the halfway point of the Linked List nodes
        if count % 2 == 0:
            halfLen = int(count / 2) + 1
        else:
            halfLen = int(count / 2) + 1

        count = 1
        current = head
        
        # Removes node at halfway
        if halfLen == 1:
            head = None
            return head
        while current:
            if count + 1 == halfLen:
                if current.next.next == None:
                    current.next = None
                    break
                else:
                    current.next = current.next.next
                    break
            else:
                current = current.next
                count += 1
        
        # Returns the head
        return head
        
