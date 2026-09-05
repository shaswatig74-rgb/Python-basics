# encapsulation - hiding sensitive information - not making them public

class Employee:
    def __init__(self, name, email, phone):
        self.name = name # public property
        self.email = email # public property
        self.__phone = phone # private property
# methods - getters and setters
    def getPhone(self):
        return self.__phone
    
    def setPhone(self, newPhone):
        self.__phone = newPhone


director = Employee("Dinesh Kumar", "dinesh@kbcgroup.com", "7547488552")

print(director.name)
print(director.email)
# print(director.__phone)
print(director.getPhone())

# changing the property values
director.email = "dineshkumar@kbcgroup.com"
print(director.email)

director.__phone = "787878787878"
print(director.getPhone())

director.setPhone("9898989898")
print(director.getPhone())

