from python.factory_method import Car

class Mercedes(Car.car_interface):
    def car_creator(self):
        print("Mercedes markasında araç oluşturuldu")