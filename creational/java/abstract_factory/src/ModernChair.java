public class ModernChair implements Chair{

    public ModernChair(){}
    @Override
    public boolean hasLegs() {
        return false;
    }
    @Override
    public boolean sitOn() {
        return true;
    }
    @Override
    public String toString() { return "Modern Chair"; }
}
