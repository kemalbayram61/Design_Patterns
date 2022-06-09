from python.factory_method import Car

class Bmw(Car.car_interface):
    def car_creator(self):
        print("Bmw markasında araç oluşturuldu")