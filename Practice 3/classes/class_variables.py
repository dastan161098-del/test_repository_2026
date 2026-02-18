# Example 1
class Car:
    wheels = 4

c1 = Car()
c2 = Car()
print(c1.wheels, c2.wheels)

# Example 2
Car.wheels = 6
print(c1.wheels, c2.wheels)

# Example 3
class Student:
    school = "NIS"

s1 = Student()
s2 = Student()
print(s1.school, s2.school)

# Example 4
Student.school = "BINOM"
print(s1.school)

# Example 5
class Game:
    level = 1

g = Game()
print(g.level)