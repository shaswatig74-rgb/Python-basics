# 4 main data structures in python: list, tuple, dictionary, sets

# list - ordered, indexed, supports duplicate values

# creating a list
names = ["Rakesh", "Mahesh", "Ganesh", "Mukesh", "Yogesh", "Dharmesh", "Naresh", "Paresh"]
print(type(names))
print(names[0])
print(names[2])
print(names[len(names) - 1])
print(names[-1])

# list can contain any data type
myList = ["Tuang", 78, 9.5, True]
# slice a list => cut part of list
colors = ["red", "blue", "green", "yellow", "black", "white" ,"orange", "pink", "violet", "red"]
print(colors[2:7])# starting index is included but ending is not included

# most used list methods
# append(value) = insert at the end of the list
colors.append("indigo")
print(colors)

# sort() => ascending order
colors.sort()
print(colors)

# sort(reverse = True) => descending order
colors.sort(reverse = True)
print(colors)

veggies = ["potato", "garlic", "ginger", "onion", " radish"]

# flip the list horizontally = reverse()
veggies.reverse()
print(veggies)

# extend() = join one list with another and return the first list
colors.extend(veggies)
print(colors)

# count(item) = return the number of times a particular item is 
print(colors.count("red"))

# index(item) => returns the index number of the first  match
print(colors.index("potato"))

# remove(item)
colors.remove("yellow")
print(colors)

# pop() => removes the last item
colors.pop()
print(colors)

# insert(index, value)
colors.insert(0, "copper")
print(colors)

# copy() - creates a duplicate list
colors1 = colors.copy()
print("------------------ colors 1----------------")
print(colors1)
print("------------------ colors 1----------------")

# clear() = clears the whole list
colors.clear()
print(colors)

# delete the list => del keyword
del colors 
# print(colors)