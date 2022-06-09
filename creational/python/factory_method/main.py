from python.factory_method.CarCreator import car_creator

brand       = "Audi"
car_creator = car_creator()
car         = car_creator.create_car(brand)
car.car_creator()