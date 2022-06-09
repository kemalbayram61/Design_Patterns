from abc      import ABC, abstractmethod

class Device(ABC):

    def __init__(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def runTest(self) ->None:
        pass

    @abstractmethod
    def endTest(self) ->None:
        pass