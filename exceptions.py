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

try:
    age = int(input("Age :"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("NO exceptions were thrown")
print("Excution continues...")
