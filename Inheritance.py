# inheritaance in python OOP
# inheritance means using the properties and methods of 1 class by another class
# super class or parent class
class Vehicle:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def info(self):
        return f"{self.color} and {self.price}"

class Plane:
    def __init__(self, regNo):
        self.regNo = regNo

# sub class or child class with single class inheritance
# class Car(Vehicle):
#  def __init__(self, color, price, brand, fuel): 
#     super().__init__(color, price)
#    self.brand = brand
#   self.fuel = fuel

# def newInfo(self):
#     return "This is the new method which replaced the old method inherited from the super class - Vehicle"

# sub class or child class with multiple class inheritance
class Car(Vehicle, Plane):
    def __init__(self, color, price, regNo, brand, fuel):
        Vehicle.__init__(self, color, price)
        Plane.__init__(self, regNo)
        self.brand = brand
        self.fuel = fuel
    def newInfo(self):
         return "This is the new method which replaced the old method inherited from the super class - Vehicle"
    
car1 = Car("White", 1000000, "QWERFDT1200", "Mahindra", "EV")

print(car1.color)

print(car1.price)

print(car1.info())

print(car1.brand)

print(car1.fuel)

print(car1.info())

print(car1.newInfo())

print(car1.regNo)
    
    


