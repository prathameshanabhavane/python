# class: blueprint for craeting new objects.
# object:Instance of class


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
# print(isinstance(point, int))
