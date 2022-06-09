from CarBuilder import CarBuilder

class HighPackCarbuilder(CarBuilder):
    def __init__(self):
        CarBuilder.__init__(self)

    def buildEngine(self) ->None:
        self._car.setEngine("w12")

    def buildInterior(self) ->None:
        self._car.setInterior("full pack interior")

    def buildHeadLight(self) ->None:
        self._car.setHeadlight("matrix")

    def buildSunroof(self) -> None:
        self._car.setSunroof("panoramical glass ceiling")