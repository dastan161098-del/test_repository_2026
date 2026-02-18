# Example 1
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.method_a()
obj.method_b()

# Example 2
class X:
    def show(self):
        print("X")

class Y:
    def show(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
z.show()  # MRO бойынша X.show шақырылады

# Example 3
class A:
    def a(self):
        print("A method")

class B:
    def b(self):
        print("B method")

class C(A, B):
    pass

c = C()
c.a()
c.b()

# Example 4
class Father:
    def skill(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

ch = Child()
ch.skill()
ch.skill2()

# Example 5
class X:
    def show(self):
        print("X")

class Y:
    def display(self):
        print("Y")

class Z(X, Y):
    pass

z = Z()
z.show()
z.display()