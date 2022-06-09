public class VictorianSofa implements Sofa{
    @Override
    public boolean hasLegs() { return true; }
    @Override
    public boolean sitOn() {
        return true;
    }
    @Override
    public String toString() { return "Victorian Sofa"; }
}
