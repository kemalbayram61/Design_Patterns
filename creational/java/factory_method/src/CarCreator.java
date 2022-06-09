public class CarCreator
{
    public Car createCar(String brand)
    {
        if (brand.equals("Audi"))
        {
            return new Audi();
        }
        else if (brand.equals("Bmw"))
        {
            return new Bmw();
        }
        else
        {
            return new Mercedes();
        }
    }
}
