# letters = ["a", "b", "c", "d"]
# matrix = [[0, 1], [1, 2], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(0, 21))
# chars = list("Hello World")
# lengthChar = len(chars)
# lengthNumbers = len(numbers)


# print(letters)
# print(letters[0])
# print(matrix)
# print(zeros)
# print(combined)
# print(numbers)
# print(chars)
# print(lengthChar)
# print(lengthNumbers)


# Accessing Items

letters = ["a", "b", "c", "d"]

letters[0] = "A"

print(letters)
print(letters[0:3])
print(letters[1:])
print(letters[:])
print(letters[::2])
print(letters[::-1])
print(letters[-1])


# numbers = list(range(0, 20))

# print(numbers[::2])
# print(numbers[::3])
# print(numbers[::-3])
# print(numbers[::-2])
# print(numbers[::-1])


# List Unpacking

numbers = [1, 2, 3, 45, 6, 8, 79, 85]

first, second, *others = numbers
# first, *others, last = numbers

print(first, second)
# print(first, last)
print(others)


# Looping over list

letters = ["a", "b", "c", "d"]

for index, letter in enumerate(letters):
    print(index, letter)


# Adding or removing items

letters = ["a", "b", "c", "d"]

# Add
letters.append("e")
letters.insert(0, "-")
print(letters)

# Remove
# letters.pop()
# letters.pop(1)
del letters[0:3]
# letters.clear()
print(letters)


# finding item
letters = ["a", "b", "c", "d"]

print(letters.count("e"))

print(letters.index("c"))
if "e" in letters:
    print(letters.index("e"))
