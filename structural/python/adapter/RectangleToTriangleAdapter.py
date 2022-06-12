from Shape     import Shape
from Rectangle import Rectangle
from Triangle  import Triangle
class RectangleToTriangleAdapter(Shape):
    __rectangle:  Rectangle = None
    __triangle:   Triangle  = None

    def __init__(self, rectangle: Rectangle):
        self.__rectangle = rectangle
        self.__triangle  = Triangle(self.__rectangle.getWidth(), self.__rectangle.getHeight())

    def draw(self) ->None:
        self.__triangle.draw()

    def getWidth(self) ->float:
        return self.__triangle.getWidth()

    def getHeight(self) ->float:
        return self.__triangle.getHeight()