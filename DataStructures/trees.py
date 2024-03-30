class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def addNode(self, value, root=self.root):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
        else:
            if value>self.root.data:
                if self.root.right is None:
                    self.root.right = newNode
                else:
                    self.addNode(value, self.root.right)
                
