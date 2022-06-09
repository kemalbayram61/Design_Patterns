public class MediumPackCarBuilder extends CarBuilder{
    @Override
    public void buildEngine() {
        this.car.setEngine("w6");
    }

    @Override
    public void buildHeadLight() {
        this.car.setHeadlight("lens");
    }

    @Override
    public void buildInterior() {
        this.car.setInterior("medium pack");
    }

    @Override
    public void buildSunroof() {
        this.car.setSunroof("sunroof");
    }
}
