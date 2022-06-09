public class HighPackCarBuilder  extends CarBuilder{
    @Override
    public void buildEngine() {
        this.car.setEngine("w12");
    }

    @Override
    public void buildHeadLight() {
        this.car.setHeadlight("matrix");
    }

    @Override
    public void buildInterior() {
        this.car.setInterior("full pack");
    }

    @Override
    public void buildSunroof() {
        this.car.setSunroof("panoramic glass ceiling");
    }
}
