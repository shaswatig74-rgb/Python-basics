# dicitionary - key:value - ordered, mutable, unique
person = {
    "fName": "Shrihan",
    "lName": "Chhotaray",
    "age": 13,
    "isNRI": True
}

# access => dictionary["key"]
print(person["fName"])
print(person["age"])

# change items
person["age"] = 23
print(person["age"])

# updating items
person.update({"isNRI":False})
print(person["isNRI"])

# check type
print(type(person))

# adding new items
person.update({"city": "Doha"})
person["fav_color"]  = "red"
print(person["city"])
print(person["fav_color"])

# remove items
# pop(key) => will remove item with key
person.pop("fName")

# popitem() => it will remove the last item
person.popitem() # fav_color is removed

# print(person["fav_color"])
# print(person["fName"])

print("----------------------------------------------------------------------------------------------")

# looping through the keys of the dicitionary
for keys in person:
    print(keys)

print("-----------------------------------------------------------------------------------------")

# looping over the values of the dictionary
for key in person:
    print(person[key])

print("---------------------------------------------------------------------------------------")

for value in person.values():
    print(value)

print("-------------------------------------------------------------------------------------------")

# looping over the items of the dicitionary
for key in person:
    print(key,":",person[key])

print("------------------------------------------------------------------------------------------------")

for key, value in person.items():
    print(key,":", value)

print("---------------------------------------------------------------------------------------------------")

# copy a dictionary

user = person.copy()
print(user["age"])




