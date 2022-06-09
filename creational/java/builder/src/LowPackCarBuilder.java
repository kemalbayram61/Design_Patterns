public class LowPackCarBuilder extends CarBuilder{
    @Override
    public void buildEngine() { this.car.setEngine("1.4TFSI"); }
    @Override
    public void buildHeadLight() {
        this.car.setHeadlight("halogen");
    }
    @Override
    public void buildInterior() {
        this.car.setInterior("low pack");
    }
    @Override
    public void buildSunroof() { this.car.setSunroof("no sunroof"); }
}
