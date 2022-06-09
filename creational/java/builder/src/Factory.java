public class Factory {
    private CarBuilder carBuilder;
    public Factory(CarBuilder carBuilder) {
        this.carBuilder = carBuilder;
    }

    public Car getCar(){
        return this.carBuilder.getCar();
    }

    public void addAttributes(){
        this.carBuilder.buildEngine();
        this.carBuilder.buildHeadLight();
        this.carBuilder.buildInterior();
        this.carBuilder.buildSunroof();
    }
}
