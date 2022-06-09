from python.factory_method import Car

class Audi(Car.car_interface):
    def car_creator(self):
        print("Audi markasında araç oluşturuldu")