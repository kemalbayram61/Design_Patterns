public class ModernSofa implements Sofa{
    @Override
    public boolean hasLegs() { return false; }
    @Override
    public boolean sitOn() { return true; }
    @Override
    public String toString(){ return "Modern Sofa"; }
}
