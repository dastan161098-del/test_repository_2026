# Example 1: *args
def sum_all(*numbers):
    print(sum(numbers))

sum_all(1, 2, 3, 4)

# Example 2: **kwargs
def print_info(**info):
    for key, value in info.items():
        print(key, value)

print_info(name="Sayaa", age=18)

# Example 3: умножение всех чисел
def multiply_all(*nums):
    result = 1
    for n in nums:
        result *= n
    print(result)

multiply_all(2, 3, 4)

# Example 4: печать kwargs красиво
def show_user(**data):
    print("User info:")
    for k in data:
        print(f"{k}: {data[k]}")

show_user(name="Sayaa", age=18, city="Talgar")

# Example 5: args + kwargs
def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1,2,3, a=10, b=20)