"""
Provided two sorted linked lists, perform a merge to result in one sorted linked list
Singular, non-cyclical
"""
# Compare value of node1 and value of node2
# if value of node 1 is less than or equal value of node 2,
# then node = ListNode(node1.val)
# node.next = merge(node1.next, node2)
# elif value of node2 < value of node 1
# then node =ListNode(node2.val)
# node.next = merge(node1, node2.next)
# return node
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    

def merge(node1, node2):
    if node1 and not node2:
        node = ListNode(node1.val)
        node.next = merge(node1.next, node2)
        return node

    elif node2 and not node1:
        node = ListNode(node2.val)
        node.next = merge(node1, node2.next)
        return node
    elif not node1 and not node2:
        pass

    elif node1.val <= node2.val:
        node = ListNode(node1.val)
        node.next = merge(node1.next, node2)
        return node

    elif node2.val < node1.val:
        node = ListNode(node2.val)
        node.next = merge(node1, node2.next)
        return node


head1 = ListNode(0)
cur = head1
for i in range(2,12,2):
    cur.next = ListNode(i)
    cur = cur.next

head2 = ListNode(1)
cur = head2
for i in range(3,12,2):
    cur.next = ListNode(i)
    cur = cur.next

cur = merge(head1, head2)
while cur.next:
    print(cur.val)
    cur = cur.next