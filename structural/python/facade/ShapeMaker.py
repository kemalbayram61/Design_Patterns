from Shape import Shape
from Circle import Circle
from Rectangle import Rectangle
from Square import Square


class ShapeMaker:
    __circle : Shape = None
    __rectangle : Shape = None
    __square : Shape = None

    def __init__(self):
        self.__circle = Circle()
        self.__rectangle = Rectangle()
        self.__square = Square()

    def draw_circle(self) -> None:
        self.__circle.draw()

    def draw_rectangle(self) -> None:
        self.__rectangle.draw()

    def draw_square(self) -> None:
        self.__square.draw()