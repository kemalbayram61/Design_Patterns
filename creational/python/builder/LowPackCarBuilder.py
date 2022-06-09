from CarBuilder import CarBuilder

class LowPackCarbuilder(CarBuilder):
    def __init__(self):
        CarBuilder.__init__(self)

    def buildEngine(self) ->None:
        self._car.setEngine("1.4TFSI")

    def buildInterior(self) ->None:
        self._car.setInterior("low pack interior")

    def buildHeadLight(self) ->None:
        self._car.setHeadlight("halogen")

    def buildSunroof(self) -> None:
        self._car.setSunroof("no sunroof")