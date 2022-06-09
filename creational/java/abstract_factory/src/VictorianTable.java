public class VictorianTable implements Table{
    @Override
    public int legCount() { return 4; }
    @Override
    public int width() { return 80; }
    @Override
    public int height() {
        return 90;
    }
    @Override
    public int depth() {
        return 120;
    }

    @Override
    public String toString() { return "Victorian Table has " + Integer.toString(this.legCount()) + " leg and width " + Integer.toString(this.width()) + " height " + Integer.toString(this.height()) + " depth " + Integer.toString(this.depth()) + "cm"   ; }
}
