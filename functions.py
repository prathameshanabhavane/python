# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("welcome aboard")


# greet("Prathamesh", "Anabhavane")

# 1. perform task
# 2. retrun value

#  1. perform task
def greet(name):
    print(f"hi {name}")


greet("prathamesh")


# 2. retrun value
# every function has default retunr value is none


def greeting(name):
    return f"hi {name}"


name = greeting("abc")

print(name)


# keyword argument
# def increament(number, by):
#     return number + by


# print(increament(2, by=1))


# default argument
def increament(number, by=1):
    return number + by


print(increament(2))


# xargs

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# xxargs

def save_user(**user):
    print(user)
    print(f"{user['name']} age is {user['age']}")


save_user(id=1, name="Jhon", age=22)

# scope glabal and local varaible

# gloabl variable
message = "a"


def greet(name):
    message = "b"  # local variable


greet("Pratham")
print(message)

# if you hae toaccess of global variable inside fucntion then have to write global keyword before the varible inside function

msg = "c"


def message():
    global msg
    msg = "d"


print(msg)
message()
print(msg)


# Exercise

# def fizz_buzz(number):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)


# fizz_buzz(3)
# fizz_buzz(5)
# fizz_buzz(15)
# fizz_buzz(7)
# fizz_buzz(30)


def fizz_buzz(number):
    if (number % 3 == 0) and (number % 5 == 0):
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return number


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(7))
print(fizz_buzz(30))
