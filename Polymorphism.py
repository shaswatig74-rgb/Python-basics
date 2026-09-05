# OOP - classes, inheritance, abstraction, encapsulation, polymorphism
# poly - same
# morphism - different forms - action is also different

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def sound(self):
        return f"{self.name} Barks"

class Cat(Animal):
    def sound(self):
        return f"{self.name} Meows"
    
class Donkey(Animal):
    def sound(self):
        return f"{self.name} Brays"

dog = Dog("Jackie")
cat = Cat("Fishy")
donkey = Donkey("Dong")

print(dog.sound())
print(cat.sound())
print(donkey.sound())
