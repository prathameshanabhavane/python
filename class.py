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
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, { self.y})")


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()
