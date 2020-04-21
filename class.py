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
class Point:
    default_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, { self.y})")


Point.default_color = "Yellow"

point = Point(1, 2)
print(point.x)
print(Point.default_color)
print(point.default_color)
print(point.y)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()
