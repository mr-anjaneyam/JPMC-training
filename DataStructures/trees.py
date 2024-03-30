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
        if root == None:
            root = newNode
        else:
            if value>root.data:
                if root.right is None:
                    root.right = newNode
                else:
                    self.addNode(value, root.right)
            else:
                if root.left == None:
                    root.left = newNode
                else:
                    self.addNode(value, root.left)

    def deleteNode(self, root, value):
        if root is None:
            return None
        else:
            if value>root.value:
                self.deleteNode(value, root.right)
            elif value<root.value:
                self.deleteNode(value, root.left)
            else:
                if root.left is None and root.right is None:
                    root = None
                elif root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
                else:
                    temp = self.minNode(root.right)
                    root.data = temp.data
                    self.deleteNode(root.right, temp.data)


    def minNode(self, root):
        if root.left is not None:
            return self.minNode(root.left)
        else:
            return root
    def maxNode(self, root):
        if root.right is not None:
            return self.maxNode(root.right)
        else:
            return root

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        print(root.data)
        if root.right is not None:
            self.inorder(root.right)
    def preorder(self, root):
        print(root.data)
        if root.left is not None:
            self.inorder(root.left)
        if root.right is not None:
            self.inorder(root.right)
    def postorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        if root.right is not None:
            self.inorder(root.right)
        print(root.data)
        
    

t = Tree()
t.addNode(4)
t.addNode(10)
t.deleteNode(10)