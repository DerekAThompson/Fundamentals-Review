class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, data, nodeBefore = None):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
            self.head.prev = self.head
        
        # Checks to see if new node will be place after a specific node before
        elif not nodeBefore:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = Node(data)
            current.next.next = self.head
            current.next.prev = current
        
        # If to be placed after a specific node
        else:
            current = self.head
            while current:
                if current.data == nodeBefore:
                    temp = current.next
                    current.next = Node(data)
                    current.next.next = temp
                    current.next.prev = current
                    break

                elif current.next is self.head:
                    print('Node does not exist')
                    break

                current = current.next
    def printLL(self):
        if not self.head:
            return print('Linked List has no nodes!!!')
        current = self.head
        while current:
            print(current.data)
            current = current.next
            if current is self.head:
                break

LL = LinkedList()
LL.printLL()
LL.insertNode(3)
LL.insertNode(72)
LL.insertNode(10)
LL.insertNode(9)
LL.insertNode(55, 3)
LL.insertNode(43)
LL.insertNode(82, 55)
LL.printLL()
print('should look like, 3, 55, 82, 72, 10, 9, 43')

