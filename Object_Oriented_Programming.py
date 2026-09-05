# object oriented programming in python - OOP
class Person:
    # constructor methods
    def __init__(self, name, age, height, isMarried):
        self.name = name
        self.age = age
        self.height = height
        self.isMarried = isMarried

    def speak(self, lang):
        return f"I can speak {lang}"
    
    def play(self, sport):
        return f"I can play {sport}"
    

person = Person("Ajay", 25, 5.11, True)

# access
print(person.name)
print(person.age)
print(person.height)
print(person.isMarried)
print(person.speak("Bangla"))
print(person.play("Football"))