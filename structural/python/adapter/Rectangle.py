from Shape import Shape
class Rectangle(Shape):
    __width:  float = 0.0
    __height: float = 0.0
    def __init__(self, width, height):
        self.__width  = width
        self.__height = height

    def draw(self) ->None:
        for i in range(self.__height):
            for j in range(self.__width):
                print("*", end="")
            print()

    def getWidth(self) ->float:
        return self.__width

    def getHeight(self) ->float:
        return self.__height