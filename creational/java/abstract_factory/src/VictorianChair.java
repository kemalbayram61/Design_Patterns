public class VictorianChair implements Chair{
    @Override
    public boolean hasLegs() {
        return true;
    }
    @Override
    public boolean sitOn() {
        return true;
    }
    @Override
    public String toString() { return "Victorian Chair"; }
}
