#Method Overriding
class A:
    def m1(self):
        print("Class A")
class B:
    def m1(self):
        print("Class B")

#Method Overloading
class C:
    def add(self, a, b):
        print(a+b)
    def add(self, a, b, c):
        print(a+b+c)
