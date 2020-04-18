import math
print('Hello World')
print('*' * 10)
x = 5
print(x)

students_count = 1000
rating = 4.99
is_publihed = True
course_name = 'Python programming'
print(students_count)
print(rating)
print(is_publihed)
print(course_name)


print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])


# \"
# \'
# \\
# \n
# course = "Python \"Programming"
# course = "Python \'Programming"
# course = "Python \\Programming"
course = "Python \nProgramming"
print(course)


first_name = "Prathamesh"
last_name = " Anabhavane"
# full_name = first_name + ' ' + last_name
full_name = f"{first_name} {last_name}"
demo = f"{len(first_name)} {2 + 2}"
# print(first_name + ' ' + last_name)
print(full_name)
print(demo)

course_name = "Python Programming"

print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.strip())
# print(course_name.lstrip())
# print(course_name.rstrip())
print(course_name.find('Pro'))
print(course_name.replace('P', 'J'))
print("Pro" in course_name)
print("Swift" not in course_name)

# numbers type
x = 1  # int
y = 4.5  # float
z = 1 + 2j  # complex
print(type(x))
print(type(y))
print(type(z))

print(3 + 5)
print(3 - 5)
print(3 * 5)
print(3 / 5)
print(3 // 5)
print(3 % 5)
print(3 ** 5)

x = 10
# x = x + 3
x += 3  # augmented assignment operator

print(x)


print(round(3.9))
print(abs(-12))
print(math.ceil(2.6))
print(math.copysign(1.0, -0.0))
print(math.factorial(5))
print(math.floor(5.6))


# Type conversion
# int()
# float()
# bool()
# str()

# x = input("x: ")
# y = int(x) + 1

# z = f"x: {x}, y: {y}"

# print(z)

# Conditional statement
temperature = 15

if temperature > 30:
    print("it's warm")
    print('You can dirnk it')
elif temperature > 20:
    print("it's nice")
else:
    print("It's cold")
print('Done')


# Ternary Operator

age = 22

message = "Eligible" if age >= 18 else "Not eligile"

print(message)
