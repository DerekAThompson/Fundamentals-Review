"""
Here is my solution to the Merge Two Sorted Lists Problem:
https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2:
                return None
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list3 = ListNode(list1.val)
            list1 = list1.next
        elif list2.val <= list1.val:
            list3 = ListNode(list2.val)
            list2 = list2.next
        merger(list1, list2, list3)
        return list3

            
def merger(list1, list2, list3):
    if not list1 and not list2:
        return
    elif list1 and not list2:
        list3.next = ListNode(list1.val)
        list3 = list3.next
        list1 = list1.next
        merger(list1, list2, list3)
    elif list2 and not list1:
        list3.next = ListNode(list2.val)
        list3 = list3.next
        list2 = list2.next    
        merger(list1, list2, list3)
    elif list1.val < list2.val:
        list3.next = ListNode(list1.val)
        list3 = list3.next
        list1 = list1.next
        merger(list1, list2, list3)
    elif list2.val <= list1.val:
        list3.next = ListNode(list2.val)
        list3 = list3.next
        list2 = list2.next  
        merger(list1, list2, list3)
    else:
        return
    return list3
            
