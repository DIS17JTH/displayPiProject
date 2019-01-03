import math

print("Hello World :D")
print("*" * 10)

print("Hello")

2+3

x: int = 1

y: int = x

unit_price = 2

print(y)

students_count = 1000
rating = 4.99
is_published = False
course_name = """
Multiple
Lines
"""
a, b = 1, 2
a = b = 1
print(id(x))

x = x + 1
print(id(x))

# lists
list = [1, 2, 3]
print(id(list))
print(list)
# lägg till
list.append(4)
print(id(list))
print(list)

# str
course = " Python Programming"
print(len(course))
print(course[0])
print(course[-1])
# slice array
print(course[0:3])
print(course[:3])
print(course[0:])
print(course[:])

print(id(course))
print(id(course[0]))

message = "Python \"programming"
print(message)
# comment
# escape seqences
# \"
# \'
# \\
# \n

# str
first = "Mosh"
last = "Hamedani"
full = f"{first} {last}"
print(full)

# formatting strings
course = " Python Programming"
print(course.upper())
print(course.strip())

print(course.find("pro"))
print(course.replace("P", "-"))

print("Programming" in course)
print("Programming" not in course)
# numbers
x = 10
x = 0b10
print(x)
# hex()
print(bin(x))

# a + bi
komplexa_tal = 1+2j
print(komplexa_tal)

# devision
c = 10 / 3
print(c)
c = 10//3
print(c)

# ** = pow()


# constants not actually constant
PI = -3.14
round(PI)
abs(PI)


# with math
print(math.floor(PI))


# type converton
print(int(x))
print(float(x))
print(bool(x))

# boolean falsy values
# Falsy
# ""
# 0
# []
# None (null)

# >= ==

if x >= 10:
    print(x)
elif x == 9:
    print("Hello")
else:
    print("Nope")

print("All done!")

if x < 10:
    pass
else:
    pass

# logical operators
name = " "
if not name.strip():
    print("Name is empty")

age = 22
if age >= 18 and age < 65:
    print("Eligible")

# 18 <= age < 65
if 18 <= age < 65:
    print("Eligible")


# new style
# message_2 = age >= 18 ? "Eligible": "Not Eligible"
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# loops
for g in "Python":
    print(g)

for h in ['a', 'b', 'c']:
    print(h)

for j in range(5):
    print(j)

for k in range(0, 10, 2):
    print(k)

# shortcuts
#shift+ alt + down
# alt+down
# ctrl+home/end
