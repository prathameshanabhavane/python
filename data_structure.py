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

# Sorting List
numbers = [3, 54, 2, 68, 79, 99]

# numbers.sort()
# numbers.sort(reverse=True)
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(numbers)


# Sort tuple with list
# items = [
#     ("Product1", 52),
#     ("Product2", 15),
#     ("Product3", 9)
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)


# Lambda Function
# Simple one line anonymous funtion so that we can pass another function

items = [
    ("Product1", 52),
    ("Product2", 15),
    ("Product3", 9)
]

items.sort(key=lambda item: item[1])
print(items)


# Map function

items = [
    ("Product1", 52),
    ("Product2", 15),
    ("Product3", 9)
]

# prices = []

# for item in items:
#     prices.append(item[1])

# print(prices)

# prices = map(lambda item: item[1], items)
# for item in prices:
#     print(item)

prices = list(map(lambda item: item[1], items))
print(prices)


# Filter Function

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)
