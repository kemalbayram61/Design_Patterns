from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self) ->None:
        pass

    @abstractmethod
    def getWidth(self) ->float:
        pass

    @abstractmethod
    def getHeight(self) ->float:
        pass