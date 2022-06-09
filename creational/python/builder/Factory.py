from CarBuilder import CarBuilder
from Car import  Car
class Factory:
    ___carBuilder: CarBuilder = None

    def __init__(self, carBuilder: CarBuilder):
        self.___carBuilder = carBuilder

    def getCar(self)->Car:
        return self.___carBuilder.getCar()

    def addAttributes(self):
        self.___carBuilder.buildEngine()
        self.___carBuilder.buildHeadLight()
        self.___carBuilder.buildSunroof()
        self.___carBuilder.buildInterior()