#1
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


#2
def count_up_to(n):
    for i in range(1, n+1):
        yield i

gen = count_up_to(5)
for num in gen:
    print(num)


#3
def squares(n):
    for i in range(n):
        yield i * i

for sq in squares(6):
    print(sq)



#4
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(8):
    print(num)


#5
def even_numbers(a, b):
    for i in range(a, b+1):
        if i % 2 == 0:
            yield i

for num in even_numbers(1, 10):
    print(num)


#6
nums = (i*i for i in range(5))

for n in nums:
    print(n)


#Iterators 
#1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


#2
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#3
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

#4
mystr = "banana"

for x in mystr:
  print(x)

#5
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))