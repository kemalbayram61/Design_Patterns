public abstract class CarBuilder {
    protected Car car;

    public void createDefaultCar(){ this.car = new Car(); }
    public Car getCar(){ return this.car; }
    public abstract void buildEngine();
    public abstract void buildHeadLight();
    public abstract void buildInterior();
    public abstract void buildSunroof();
}
