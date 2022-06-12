from Rectangle                  import Rectangle
from Triangle                   import Triangle
from RectangleToTriangleAdapter import  RectangleToTriangleAdapter
if __name__ == "__main__":
    rectangle: Rectangle = Rectangle(10,20)
    rectangle.draw()
    print("###########################################################")
    adapter: RectangleToTriangleAdapter = RectangleToTriangleAdapter(rectangle)
    triangle: Triangle = adapter
    triangle.draw()