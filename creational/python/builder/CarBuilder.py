from abc import ABC, abstractmethod
from Car import Car

class CarBuilder(ABC):
    _car: Car = None

    def createDefaultCar(self)->None:
        self._car = Car()

    def getCar(self)->Car:
        return self._car

    @abstractmethod
    def buildEngine(self)->None:
        pass

    @abstractmethod
    def buildHeadLight(self)->None:
        pass

    @abstractmethod
    def buildInterior(self)->None:
        pass

    @abstractmethod
    def buildSunroof(self) -> None:
        pass