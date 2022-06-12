from Shape import Shape
class Triangle(Shape):
    __width:  float = 0.0
    __height: float = 0.0
    def __init__(self, width, height):
        self.__width  = width
        self.__height = height

    def draw(self) ->None:
        width:int = 1
        for i in range(self.__height):
            for j in range(self.__height - width):
                print(" ", end="")
            for j in range(width * 2):
                print("*", end="")
            width = width + 1
            print()

    def getWidth(self) ->float:
        return self.__width

    def getHeight(self) ->float:
        return self.__height