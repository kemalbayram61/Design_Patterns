class Car:
    __engine:str    = None
    __headlight:str = None
    __sunroof:str   = None
    __interior:str  = None

    def getEngine(self)-> str:
        return self.__engine

    def getHeadlight(self)->str:
        return self.__headlight

    def getSunroof(self)->str:
        return self.__sunroof

    def getInterior(self)->str:
        return self.__interior

    def setEngine(self, engine: str)->str:
        self.__engine = engine
        return  self.__engine

    def setHeadlight(self, headlight: str)->str:
        self.__headlight = headlight
        return  self.__headlight

    def setSunroof(self, sunroof: str)->str:
        self.__sunroof = sunroof
        return  self.__sunroof

    def setInterior(self, interior: str)->str:
        self.__interior = interior
        return  self.__interior