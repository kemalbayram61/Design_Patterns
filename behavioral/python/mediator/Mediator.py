from Telephone import Telephone
from Computer  import Computer
from Tablet    import Tablet

class Mediator:
    __telephone: Telephone = None
    __computer:  Computer  = None
    __tablet:    Tablet    = None

    def setTelephone(self, telephone: Telephone) ->None:
        self.__telephone = telephone

    def getTelephone(self) ->Telephone:
        return self.__telephone

    def setComputer(self, computer: Computer) ->None:
        self.__computer = computer

    def getComputer(self) ->Computer:
        return self.__computer

    def setTablet(self, tablet: Tablet) ->None:
        self.__tablet = tablet

    def getTablet(self) ->Tablet:
        return self.__tablet

    def runTelephone(self) ->None:
        self.__computer.endTest()
        self.__tablet.endTest()

    def runTablet(self) ->None:
        self.__computer.endTest()
        self.__telephone.endTest()

    def runComputer(self) ->None:
        self.__telephone.endTest()
        self.__tablet.endTest()