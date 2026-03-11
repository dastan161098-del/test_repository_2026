#1
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

#2
# Read entire file
with open("sample.txt", "r") as f:
    print(f.read())

#3
# Read line by line
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
        
#4
# Read first 3 lines
with open("sample.txt", "r") as f:
    for i in range(3):
        print(f.readline().strip())