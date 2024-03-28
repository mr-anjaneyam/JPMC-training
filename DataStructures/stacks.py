stack = []
length = int(input("Enter the length of stack: "))
class Stack:
    def Push(self, element):
        if len(stack) >= length:
            print("*****Stack Overflow*****")
            return
        stack.append(element)
        print("Element inserted successfully")
    def Pop(self):
        if self.isEmpty():
            print("*****Stack Underflow*****")
            return
        stack.pop()
        print("Element popped out")
    def isEmpty(self):
        return len(stack) == 0
    def Top(self):
        return stack[-1]
    def Display(self):
        print(stack)
        return

s = Stack() 
while True:
    print("\n1. Push Element\n2. Pop Element\n3. Display Stack\n4. Peek\nAny other number to exit\n")
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