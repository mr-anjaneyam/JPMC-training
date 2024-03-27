from abc import ABC, abstractmethod

class Fruit(ABC): #inheriting from abstract base class
    @abstractmethod #annotation to mention this as abstract method explicitly
    def getColor(self):
        pass #No statements are to be written in abstract method
    def getPrice(self):
        return 100

class Test(Fruit):
    def getColor(self):
        print("Fruit color is red")
    def getName(self):
        print("It is a Mango!")
    
t = Test()
t.getColor()
t.getName()
print(t.getPrice())