import os
import shutil

# with open("index.js", "a") as file:
#    file.write("console.log("Hello World");")

# with open("index.js",  "r") as file:
#   print(file.read())

# with open("index.js",  "x") as file:
#   print("file created")

# removing a file
# os.remove("index.js")

# creating a folder
# os.mkdir("sample")

# creating a file inside the folder
# with open("sample/test.txt", "a") as file:
#   file.write("Hello World")

# removing a folder
# os.rmdir("sample") #  it will remove only if the folder is empty

shutil.rmtree("sample") # it will force remove a non empty folder.

# create folder

# os.mkdir("folder name")

# remove a file

# os.remove("file name")

# remove an empty folder

# os.rmdir("folder name")

# check where a file exists or not

os.path.exists("main.js") # True

# renaming a file

# os.rename("index.js", "main.js")

# list the folder content

os.listdir("sample_data")

# check if file - True means file and False means not a file

print(os.path.isfile("sample_data"))

# check if directory - True means file and False means not a directory

print(os.path.isdir("sample_data"))

print(os.system("ls"))




