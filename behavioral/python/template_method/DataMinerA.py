from abc import  ABC, abstractmethod

class DataMiner(ABC):
    @abstractmethod
    def openFile(self, path: str) ->str:
        pass

    @abstractmethod
    def extractData(self, file: str) ->str:
        pass

    @abstractmethod
    def parseData(self, data: str) ->str:
        pass

    @abstractmethod
    def analyzeData(self, data: str) ->str:
        pass

    @abstractmethod
    def sendReport(self, data: str) ->None:
        pass

    @abstractmethod
    def closeFile(self, file: str) ->None:
        pass