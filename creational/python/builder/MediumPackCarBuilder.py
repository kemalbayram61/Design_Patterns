from CarBuilder import CarBuilder

class MediumPackCarbuilder(CarBuilder):
    def __init__(self):
        CarBuilder.__init__(self)

    def buildEngine(self) ->None:
        self._car.setEngine("w12")

    def buildInterior(self) ->None:
        self._car.setInterior("medium pack interior")

    def buildHeadLight(self) ->None:
        self._car.setHeadlight("lens")

    def buildSunroof(self) -> None:
        self._car.setSunroof("sunroof")