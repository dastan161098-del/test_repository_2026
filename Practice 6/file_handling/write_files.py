#1
with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python practice\n")
    f.write("File handling example\n")

print("File written successfully")

#2
# Write new file
with open("sample.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python File Handling\n")

#3
# Append new lines
with open("sample.txt", "a") as f:
    f.write("New appended line\n")

#4
# Write list to file
fruits = ["Apple", "Banana", "Orange"]

#5
with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")