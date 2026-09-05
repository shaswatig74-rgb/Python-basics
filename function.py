# functions in python
# how to create function in python
def printName():
    print("Roy")

printName()

def printFullName(fName, lName):
    print(f"{fName} {lName}")

printFullName("Shrihan", "Chhotaray")

# function with return statement
# return statement returns a value and marks the end of the function(exists the function)
def addNums(num1, num2):
    return num1 + num2 # function exists here
    print(Hey) # this will never run

result = addNums(10, 15) # will return a value of 25 to us
print(result)

if result > 20:
    print("Good Job")

# positional arguments and keyword arguments

def tellStory(character, place, time):
    print(f"Long time ago there was a hero called {character} who used to live in {place} in the {time} era") 

tellStory("Hercules", "Athens", "Medieval")
tellStory("Medieval", "Hercules", "Athens")
# positional arguments are those arguments which have to follow the order set by parameters. If the order is not followed then the result is unexpected

# key word arguments
tellStory(time = "golden", character = "Ashoka", place = "India")

# *args and **kwargs

def youngest(*kids):
    print("The youngest kid is " + kids[2])

youngest("Ravi", "Kavi", "Havi", "Tubi")

# if you combine *args with positional arguments then *args must the last

def greeting(greet, *names):
    for name in names:
        print(greet, name)

greeting("Hello", "Ravi", "Kavi", "Havi", "Tubi")

greeting("Hi", "Dave", "Kave", "Cave", "Mave")

#**kwargs

def warakkam(greet, **names):
    for key in names:
        print(greet, names[key])


warakkam("Warrkam", first="Ravi", second="Kavi", third="Havi", fourth="Tubi")

# lambda fuction
# a lambda function is a small and anonymous function. It can take any number of parameters but will always have 1 expression
# lambda parameters: expression

result = lambda num1, num2: num1+num2
print(result(10, 25)) 

full_name = lambda fName, lName: f"{fName} {lName}"
print(full_name("Akash", "Malhotra"))

def myFunction(n):
    return lambda a: a*n
doubler = myFunction(2)
print(doubler(11))
print(doubler(44))

# map(function, iterator)

number = [1,2,3,4,5]
double = list(map(lambda x: x*2, number))
print(double)

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = list(filter(lambda x: x%2 == 1, numbers))
print(odd_numbers)
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

# sorted(iterator, key=function)

students = [("Emil", 25), ("Teddy", 22), ("Jacob", 28), ("Walter", 19), ("Henry", 30)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

fruits = ["watermelon", "cherry", "apple", "Kiwi", "banana"]
sorted_fruits = sorted(fruits, key=lambda fruit: len(fruit))
print(sorted_fruits)