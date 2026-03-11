#1
names = ["Ali", "Dana", "Sara"]
scores = [85, 90, 88]

for i, name in enumerate(names):
    print(i, name)

for name, score in zip(names, scores):
    print(name, score)

#2
names = ["Ali", "Dana", "Sara"]
scores = [85, 90, 88]

# enumerate()
for i, name in enumerate(names, start=1):
    print(i, name)

# zip()
for name, score in zip(names, scores):
    print(name, score)

# zip to dictionary
students = dict(zip(names, scores))
print(students)