class Node:
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data    


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


    def InOrderTraversal(self, root):
        res = []
        if root:
            res = self.InOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.InOrderTraversal(root.right)
        return res


    def PreOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res
    

    def PostOrderTraversal(self, root):
        res = []
        if root:
            res = self.PostOrderTraversal(root.left)
            res = res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res


# Checks Generic Tree
root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()



# Checks In Order Traversal
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.InOrderTraversal(root))  



# Checks Pre Order Traversal
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PreOrderTraversal(root))


# Checks Post Order Traversal
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PostOrderTraversal(root))
