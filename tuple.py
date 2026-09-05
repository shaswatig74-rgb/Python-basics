# tuple - just like list  ordered, indexed, allows duplicates , immutable 
fruits = ("apple", "orange", "kiwi", "apple")
veggies = tuple(("tomato", "potato"))
print(type(fruits))
print(type(veggies))

# indexed
print(fruits[0])
print(veggies[1])

# length  of tuple
print(len(fruits))

# slicing a tuple
print(fruits[1:3])

# updating a tuple - by converting it into a list
fruitList = list(fruits)
print(type(fruitList))
fruitList.append("grapes")
fruits = tuple(fruitList)
print(fruits[-1])
print(len(fruits))

# tuple
# unpacking
fruits = ("apple", "guava", "banana")
(red , green, yellow) = fruits
print(red) # red = "apple"
print(green) # green = "guava"
print(yellow) # yellow = "banana"

moreFruits = ("blueberry", "kiwi", "blackberry", "cherry" , "coconut", "pineapple")
(blue, brown, black, *basket) = moreFruits
print(blue)
print(black)
print(brown)
print(basket)
print(type(basket))

# looping through the tuple
for fruit in fruits:
    print(fruit)

print("----------------------------------------------------------------------")

# while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

print("----------------------------------------------------------------------")

# range
for i in range(len(fruits)):
    print(fruits[i])

# joining the  tuples
# we can join tuples using the + operator => return a new tuple
colors1 = ("red", "green", "blue")
colors2 = ("Orange", "yellow", "white")

colors3 = colors1 + colors2
print(colors3)

# count(items)
veggies = ("potato", "tomato", "chilli", "onion", "onion", "potato", "potato")
print(veggies.count("onion"))
print(veggies.count("potato"))

# index() - returns the index of the first match
print(veggies.index("onion"))



