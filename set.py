# sets = unordered, unindexed, immutable, unique
fruits = {"apple", "orange", "Kiwi"}
print(fruits)
print(type(fruits))

# create using constructor
veggies = set(("potato", "chilli"))
print(veggies)
print(type(veggies))

# accessing set items - no way through index numbers or keys
# only way to access is to loop over the set
for fruit in fruits:
  print(fruit)

# boolean return using "in" or "not in" memberships operators
print("orange" in fruits)
print("grapes" in fruits)
print("grapes" not in fruits)

fruits = {"apple", "orange", "Kiwi"}

veggies = set(("potato", "chilli"))
colors = ("red", "blue", "green")
cars = ["toyota", "hyundai", "ferrari"]
person = {
    "name": "Kishore",
    "age": 20
}

# add new item to the fruits set
fruits.add("fig")
print(fruits)

# update method
fruits.update(veggies)
print(fruits)

fruits.update(colors)
print(fruits)

fruits.update(cars)
print(fruits)

fruits.update(person)
print(fruits)

# removal of set items
fruits.remove("name")
print(fruits)

fruits.discard("mahindra") # discard method does not produce any error in case the item is not present

# pop() - it removes any random item from the set
removedItem = fruits.pop()
print(removedItem)
print(fruits)

# # clear() - empties the whole set
# fruits.clear()
# print(fruits)

# # del keyword - deletes the set
# del fruits
# print(fruits)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"x", "y", "z"}

# union() - join the sets and returns a new set
# union_update() - modifies or updates the existing set
newSet = set1.union(set2, set3)
print(newSet)

fruits1 = {"apple","ornage", "coconut", "banana"}
fruits2 = {"pineapple","ornage", "fig", "banana"}

# intersection() - returns a new set with common items
# intersection_update()- modifies or updates the existing set
fruits3 = fruits1.intersection(fruits2)
print(fruits3)

# difference() - returns a new set with uncommon items of the first set
# difference_update()- modifies or updates the existing set
fruits4 = fruits2.difference(fruits1)
print(fruits4)

# symmetric_difference() - returns a new set with uncommon items
# symmetric_difference_update()- modifies or updates the existing set
fruits5 = fruits1.symmetric_difference(fruits2)
print(fruits5)