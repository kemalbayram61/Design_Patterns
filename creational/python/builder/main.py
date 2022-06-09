from CarBuilder           import  CarBuilder
from HighPackCarBuilder   import  HighPackCarbuilder
from LowPackCarBuilder    import  LowPackCarbuilder
from MediumPackCarBuilder import MediumPackCarbuilder
from Factory              import Factory
from Car                  import Car

def main():
    hCarBuilder: CarBuilder = HighPackCarbuilder()
    mCarBuilder: CarBuilder = MediumPackCarbuilder()
    lCarBuilder: CarBuilder = LowPackCarbuilder()

    hCarBuilder.createDefaultCar()
    mCarBuilder.createDefaultCar()
    lCarBuilder.createDefaultCar()

    hFactory: Factory = Factory(hCarBuilder)
    mFactory: Factory = Factory(mCarBuilder)
    lFactory: Factory = Factory(lCarBuilder)

    hFactory.addAttributes()
    mFactory.addAttributes()
    lFactory.addAttributes()

    hCar: Car = hFactory.getCar()
    mCar: Car = mFactory.getCar()
    lCar: Car = lFactory.getCar()

    print("#################->High Car")
    print(hCar.getEngine())
    print(hCar.getSunroof())
    print(hCar.getHeadlight())
    print(hCar.getInterior())

    print("#################->Medium Car")
    print(mCar.getEngine())
    print(mCar.getSunroof())
    print(mCar.getHeadlight())
    print(mCar.getInterior())

    print("#################->Low Car")
    print(lCar.getEngine())
    print(lCar.getSunroof())
    print(lCar.getHeadlight())
    print(lCar.getInterior())

if __name__ == '__main__':
    main()