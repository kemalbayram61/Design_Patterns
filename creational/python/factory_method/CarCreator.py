from python.factory_method.Audi     import Audi
from python.factory_method.Mercedes import Mercedes
from python.factory_method.Bmw      import Bmw
from python.factory_method.Car      import car_interface
class car_creator:
    def create_car(self, brand) -> car_interface:
        if(brand == "Audi"):
            return Audi()
        elif(brand == "Bmw"):
            return Bmw()
        else:
            return Mercedes()
