try:
    age = int(input("Age :"))
except ValueError as ex:
    print("You didn't enter a valid age")
    print(ex)
    print(type(ex))
else:
    print("NO exceptions were thrown")
print("Excution continues...")
