#1
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#2
x = abs(-7.25)

print(x)

#3
x = pow(4, 3)

print(x)

#4
import math

x = math.sqrt(64)

print(x)

#5
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1

#6
import math

x = math.pi

print(x)



#EXERCISES
#1
import math

degree = float(input("Input degree: "))
radian = degree * math.pi / 180

print("Output radian:", round(radian, 6))

#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2

print("Expected Output:", area)

#3
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", round(area))

#4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height

print("Expected Output:", float(area))