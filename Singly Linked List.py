# Generates Class for Nodes of Linked List to indicate the value of the current node
# and to indicate which node is next on the Linked List
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Generates Class for Linked List to indicate the node which is the head
class LinkedList:
    def __init__(self):
        self.head = None
    # Adds a new node to the Linked List
    def insert(self,data):
        newNode = Node(data)

        # When head of Linked List exists, traverses Linked List until no next node exists
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        
        # When no head of the Linked List exists, assigns the new node as the head
        else:
            self.head = newNode
    
    # Prints Linked List
    def printLL(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # Finds if a node of a certain value exists in the Linked List       
    def findNode(self, value):
        current = self.head
        while current:
            if current.data == value:
                return print(True)
            current = current.next
        return print(False)

    # Removes nodes of a specific value from the Linked List
    def removeNode(self, value):
        current = self.head
        prev = None
        while current:
            if self.head.data == value:
                self.head = self.head.next
            elif current.data == value:
                prev.next = current.next
            prev = current
            current = current.next










LL = LinkedList()
LL.insert(7)
LL.insert(71)
LL.insert(33)
LL.insert(46)
LL.insert(93)
LL.insert(2)
LL.insert(467)
LL.printLL()
LL.findNode(2)
LL.findNode(23)
LL.removeNode(7)
LL.removeNode(93)
print('Modified LL')
LL.printLL()
