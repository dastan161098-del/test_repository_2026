# Example 1
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Ali")
print(p1.name)

# Example 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pt = Point(2, 3)
print(pt.x, pt.y)

# Example 3
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("Toyota", 2020)
print(c.brand, c.year)

# Example 4
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

r = Rectangle(3,4)
print(r.w * r.h)

# Example 5
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student("Ali", 90)
print(s.name, s.score)