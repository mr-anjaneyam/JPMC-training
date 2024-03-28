queue = []
length = int(input("Enter the length of Queue: "))
class Queue:
    def Push(self, element):
        if len(queue) >= length:
            print("*****Queue Overflow*****")
            return
        queue.append(element)
        print("Element inserted successfully")
    def Pop(self):
        if self.isEmpty():
            print("*****Queue Underflow*****")
            return
        queue.pop(0)
        print("Element popped out")
    def isEmpty(self):
        return len(queue) == 0
    def Top(self):
        return queue[-1]
    def Display(self):
        print(queue)
        return

s = Queue() 
while True:
    print("\n1. Push Element\n2. Pop Element\n3. Display Queue\n4. Peek\nAny other number to exit\n")
    op = int(input("Enter choice: "))
    if op==1:
        n = input("Enter element: ")
        s.Push(n)
    elif op==2:
        s.Pop()
    elif op==3:
        s.Display()
    elif op==4:
        print(s.Top())
    else:
        print("Hasta la Vista!")
        break