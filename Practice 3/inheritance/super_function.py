# Example 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Askar", 10)
print(s.name, s.grade)

# Example 2
class A:
    def __init__(self):
        print("A init")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init")

B()

# Example 3
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Rex", "Shepherd")
print(d.name, d.breed)

# Example 4
class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

B()

# Example 5
class Person:
    def __init__(self, age):
        self.age = age

class Student(Person):
    def __init__(self, age, grade):
        super().__init__(age)
        self.grade = grade

s = Student(18, 12)
print(s.age, s.grade)