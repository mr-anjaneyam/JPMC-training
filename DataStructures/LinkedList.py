class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def addElement(self, data):
        node=Node(data)
        if self.head==None:
            self.head=node
            return
        curr=self.head
        while(curr.next):
            curr=curr.next
        curr.next=node

        
    def display(self):
        curr=self.head
        while(curr):
            print(curr.data,end= " -> ")
            curr=curr.next
            


    def removeElement(self, value):
        curr=self.head
        prev=None
        if curr.data==value:
            self.head=curr.next
            return True
        while curr.next and curr.data!=value:
            pre=curr
            curr=curr.next
        if curr.data==value:
            pre.next=curr.next
        else:
            return False
    def search(self,value):
        curr=self.head
        
        while curr and curr.data!=value:
            curr=curr.next

        if curr.data==value:
            print("Value Found")
        else:
            print("Not Found")


        

l=Linkedlist()
l.addElement(5)
l.addElement(6)
l.addElement(9)
l.removeElement(6)
l.search(5)
l.display()