# class: blueprint for craeting new objects.
# object:Instance of class


# class Point:
#     def draw(self):
#         print("draw")


# point = Point()
# print(type(point))
# print(isinstance(point, Point))
# print(isinstance(point, int))


# Constructors
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, { self.y})")


# point = Point(1, 2)
# print(point.x)
# print(point.y)
# point.draw()


# class vs instance attribute
# class Point:
#     default_color = "Red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, { self.y})")


# Point.default_color = "Yellow"

# point = Point(1, 2)
# print(point.x)
# print(Point.default_color)
# print(point.default_color)
# print(point.y)
# point.draw()

# another = Point(3, 4)
# print(another.default_color)
# another.draw()

# class vs Instance method
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def draw(self):
#         print(f"Point ({self.x}, { self.y})")


# point = Point.zero()
# point.draw()


# magic methods
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def draw(self):
#         print(f"Point ({self.x}, { self.y})")


# point = Point(1, 2)
# print(str(point))

# Comparing objects
# https://rszalski.github.io/magicmethods/#comparisons

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(1, 2)
# other = Point(1, 2)
# another = Point(10, 50)

# print(point == other)
# print(another > other)

# performing arithmatic operations

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(1, 2)
# other = Point(1, 2)
# combined = point + other

# print(combined.x)
# print(combined.y)

# Making custom container
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def setitem(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("python")


# private members

print(cloud["PYTHON"])
print(cloud.__dict__)
print(cloud._TagCloud__tags)


# Priperties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value


product = Product(-50)
print(product.price)
