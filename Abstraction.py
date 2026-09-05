# abstraction -

# an abstract class is just like a blue print - it decides the structure but not the details

from abc import ABC, abstractmethod

# main class

class Animal(ABC):

    @abstractmethod

    def sound(self):

        pass

    @abstractmethod

    def color(self):

        pass

class Dog(Animal):

    def sound(self):

        print("bark")


    def color(self):

        print("Black")

class Cat(Animal):

    def sound(self):

        print("Meow")

    def color(self):

        print("white")

dog = Dog()

cat = Cat()

dog.sound()

cat.sound()

dog.color()

cat.color()