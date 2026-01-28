#Python Strings
#1
print("Hello")
print('Hello')

#2
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#3
a = "Hello"
print(a)

#4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#6
a = "Hello, World!"
print(a[1])

#7
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#8
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Python-Slicing Strings
#1
b = "Hello, World!"
print(b[2:5])

#2
b = "Hello, World!"
print(b[:5])

#3
b = "Hello, World!"
print(b[2:])

#4
b = "Hello, World!"
print(b[-5:-2])

#Python-Modify Strings
#1
a = "Hello, World!"
print(a.upper())

#2
a = "Hello, World!"
print(a.lower())

#3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#4
a = "Hello, World!"
print(a.replace("H", "J"))

#5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Python-String Concatenetion
#1
a = "Hello"
b = "World"
c = a + b
print(c)

#2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#Python-Format-Strings
#1
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

#2
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#3
price = 59
txt = f"The price is {price} dollars"
print(txt)

#4
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#5
txt = f"The price is {20 * 59} dollars"
print(txt)

#Python-Escape Characters
#1
txt = "We are the so-called \"Vikings\" from the north."

#2
x = "name\nage"

#3
print("Helloo\b")

#4
print("\x41")

#5
print(r"C:\new\test")


#Python - String Methods
#1
s = "hello world"
print(s.upper())

#2
s = "hello world"
print(s.replace("world", "Python"))

#3
s = "hello world"
print(s.find("world"))



