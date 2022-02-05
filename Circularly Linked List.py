class Node():
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertNode(self, data):
        if self.head:
            current = self.head
            while current:
                if current.next is self.head:
                    current.next = Node(data)
                    current.next.next = self.head
                    break
                else:
                    current = current.next
        else:
            self.head = Node(data)
            self.head.next = self.head
            
    def printLL(self):
        current = self.head
        while current:
            if current.next is self.head:
                print(current.data)
                print(current.next.data, 'head again')
                break
            else:
                print(current.data)
                current = current.next

LL = LinkedList()
LL.insertNode(8)
LL.insertNode(38)
LL.insertNode(33)
LL.insertNode(65)
LL.insertNode(3)
LL.insertNode(7)
LL.printLL()