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
def increament(number, by):
    return number + by


print(increament(2, by=1))
