# Example 1
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print(squares)

# Example 2
names = ["ali", "beka", "dana"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)

# Example 3: увеличить каждый элемент
nums = [1,2,3]
plus_one = list(map(lambda x: x+1, nums))
print(plus_one)

# Example 4: перевод в int
str_nums = ["1","2","3"]
ints = list(map(lambda x: int(x), str_nums))
print(ints)

# Example 5: квадрат + 1
nums = [2,3,4]
res = list(map(lambda x: x*x + 1, nums))
print(res)