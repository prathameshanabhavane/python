from collections import namedtuple
from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TestBox(UIControl):
    def draw(self):
        print("Text box")


class DropDownList(UIControl):
    def draw(self):
        print("Dropdowan list")


# def draw(control):
#     control.draw()

def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TestBox()

# draw(textbox)
# draw(ddl)
draw([ddl, textbox])


# Duck Type

class TestBox:
    def draw(self):
        print("Text box")


class DropDownList:
    def draw(self):
        print("Dropdowan list")


def draw(controls):
    for control in controls:
        control.draw()


draw([ddl, textbox])


# Extending built in types

class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")

# print(text.lower())
# print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()

list.append("1")
list.append("Hello")


# Data class

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
# p1 = Point(x=10, y=20)
p2 = Point(x=1, y=2)

print(p1 == p2)
