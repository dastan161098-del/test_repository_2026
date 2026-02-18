# Example 1: positional arguments
def add(a, b):
    print(a + b)

add(3, 4)

# Example 2: default argument
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("Samat")

# Example 3: именованные аргументы
def power(base, exp):
    print(base ** exp)

power(exp=3, base=2)

# Example 4: несколько аргументов
def info(name, age, city):
    print(name, age, city)

info("Ali", 18, "Astana")

# Example 5: default + обычный аргумент
def greet(name, msg="Welcome"):
    print(f"{msg}, {name}")

greet("Dana")
greet("Aigul", "Hello")