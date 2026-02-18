# Example 1
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()

# Example 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, a):
        self.a = a
    def area(self):
        return self.a * self.a

sq = Square(4)
print(sq.area())

# Example 3
class Bird:
    def sound(self):
        print("Some bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

Sparrow().sound()

# Example 4
class Worker:
    def work(self):
        print("Working...")

class Programmer(Worker):
    def work(self):
        print("Coding...")

Programmer().work()

# Example 5
class Animal:
    def move(self):
        print("Animal moves")

class Fish(Animal):
    def move(self):
        print("Fish swims")

Fish().move()