# Example 1
class Student:
    count = 0

    def __init__(self):
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

s1 = Student()
s2 = Student()
print(Student.get_count())

# Example 2
class Math:
    @classmethod
    def info(cls):
        print("This is Math class")

Math.info()

# Example 3
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show(cls):
        print("Created:", cls.count)

Counter()
Counter()
Counter.show()

# Example 4
class School:
    name = "High School"

    @classmethod
    def school_name(cls):
        print(cls.name)

School.school_name()

# Example 5
class Example:
    @classmethod
    def hello(cls):
        print("Hello from class method")

Example.hello()