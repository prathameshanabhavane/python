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
