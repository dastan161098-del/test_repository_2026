#1
from functools import reduce

numbers = [1,2,3,4,5]

squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

#2
from functools import reduce

numbers = [1,2,3,4,5]

# map()
squares = list(map(lambda x: x**2, numbers))
print("Squares:", squares)

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# reduce()
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# 2 reduce example
product = reduce(lambda x,y: x*y, numbers)
print("Product:", product)