# try:
#     age = int(input("Age :"))
# except ValueError as ex:
#     print("You didn't enter a valid age")
#     print(ex)
#     print(type(ex))
# else:
#     print("NO exceptions were thrown")
# print("Excution continues...")


# Handling different exceptions

# try:
#     age = int(input("Age :"))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("NO exceptions were thrown")
# print("Excution continues...")

# Cleaning Up
# try:
#     file = open("exceptions.py")
#     age = int(input("Age :"))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("NO exceptions were thrown")
# finally:
#     file.close()

# The with statement

# try:
#     with open("exceptions.py") as file:
#         print("file opend")
#     age = int(input("Age :"))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age")
# else:
#     print("NO exceptions were thrown")


# Raising exception

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-10)
except ValueError as error:
    print(error)
