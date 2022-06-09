public class Main
{
    public static void main(String[] args)
    {
        CarBuilder carBuilder = new HighPackCarBuilder();
        //CarBuilder carBuilder = new MediumPackCarBuilder();
        //CarBuilder carBuilder = new LowPackCarBuilder();

        carBuilder.createDefaultCar();

        Factory factory = new Factory(carBuilder);

        factory.addAttributes();

        Car car = factory.getCar();

        System.out.println(car.getEngine());
        System.out.println(car.getHeadlight());
        System.out.println(car.getInterior());
        System.out.println(car.getSunroof());
    }
}
