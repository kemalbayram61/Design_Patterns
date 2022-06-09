public class Main
{
    public static void main(String[] args)
    {
        String brand  = "Audi";
        CarCreator cc = new CarCreator();
        Car car       = cc.createCar(brand);
        car.carCreator();
    }
}
