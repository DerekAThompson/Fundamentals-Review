## Make a BST


class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

    
    def insert(self, data):
        if not self.data:
            self.data = data
            return
        if self.data > data:
            if not self.left:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if not self.right:
                self.right = Node(data)
            else:
                self.right.insert(data)
        return


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node(7)
root.insert(3)
root.insert(12)
root.insert(4)
root.PrintTree()