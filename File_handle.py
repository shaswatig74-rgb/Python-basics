# file handling using python
# open, - read mode, write mode, apppend mode
# opend a file in write mode
# when we open file in write mode - if the file already exists it open that file but if the file does not exist it will create the file
# when we write to the file opened in write mode - any new content written will completely overwrite the old/existing content
file = open("sample_write.txt", "w")
# once file is opened/created - write to the file
file.write("New text")
# close the file
file.close()

# open a file in read mode
file = open("sample_write.txt", "r")
# reading the whole file content
content = file.read()
print(content)
# close the file
file.close()

file = open("sample_read.txt", "r")
content = file.read()
print(content)
file.close()


import os

if os.path.exists("rambo.txt"):
  file = open("rambo.txt", "r")
  content = file.read()
  print(content)
  file.close()
else:
  userInput = input("Do you wish to create the file? y/n: ")
  if userInput == "y":
    # creating the file in the append mode - it lets you keep the original or old content and adding the new content
    file = open("rambo.txt", "a")
    file.write("This is a content written in the append mode")
    file.close()
  else:
    print("Alright, the was not created!")

file = open("rambo.txt", "r")
content = file.read(10)
print(content)
file.close()

file = open("sample_read.txt", "r")
# readline method only reads one line at a time
content = file.readline()
content2 = file.readline()
content3 = file.readline()
print(content)
print(content2)
print(content3)
file.close()

file = open("sample_read.txt", "r")
content = file.readlines()
print(content)
print(type(content))
print(len(content))
file.close()

for line in content:
  print(line)