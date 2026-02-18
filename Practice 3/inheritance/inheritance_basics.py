# Example 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()

# Example 2
class Bird(Animal):
    def fly(self):
        print("Bird can fly")

b = Bird()
b.speak()
b.fly()

# Example 3
class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    pass

Child().show()

# Example 4
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

Car().move()

# Example 5
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    pass

Circle().draw()