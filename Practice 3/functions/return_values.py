# Example 1
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)

# Example 2
def is_even(n):
    return n % 2 == 0

print(is_even(6))
print(is_even(7))

# Example 3: вернуть строку
def full_name(first, last):
    return first + " " + last

print(full_name("Ali", "Khan"))

# Example 4: максимум из двух
def maximum(a, b):
    return a if a > b else b

print(maximum(10, 7))

# Example 5: список квадратов
def squares(n):
    return [i*i for i in range(n)]

print(squares(5))