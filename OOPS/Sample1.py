#Parent classes
class A:
    def a1(self):
        print("a1 of class A")
    def a2(self):
        print("a2 of class A")
class B:
    def b1(self):
        print("b1 of class B")
    def b2(Self):
        print("b2 of class B")

#Inheriting class A in C - Single inheritance
class C(A):
    def c1(self):
        print("c1 of class C")
    def c2(self):
        print("c2 of class C")

#Inheriting class C in D - Multilevel inheritance
class D(C):
    def d1(self):
        print("d1 of class D")
    def d2(self):
        print("d2 of class D")

#Inheriting classes A into E, F - Hierarchical Inheritance
class E(A):
    def e1(self):
        print("e1 of class E")
    def e2(self):
        print("e2 of class E")
class F(A):
    def f1(self):
        print("f1 of class F")
    def f2(self):
        print("f2 of class F")
    
#Inheriting classes A,B into G - Multiple Inheritance
class G(A,B):
    def g1(self):
        print("g1 of class G")
    def g2(self):
        print("g2 of class G")

#creating objects
a = A()
b = B()
c = C()
d = D()
e = E()
f = F()
g = G()

