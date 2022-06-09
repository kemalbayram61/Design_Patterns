public class ModernTable implements Table{
    @Override
    public int legCount() { return 1; }
    @Override
    public int width() { return 30; }
    @Override
    public int height() {
        return 10;
    }
    @Override
    public int depth() {
        return 20;
    }
    @Override
    public String toString() { return "Modern Table has " + Integer.toString(this.legCount()) + " leg and width " + Integer.toString(this.width()) + " height " + Integer.toString(this.height()) + " depth " + Integer.toString(this.depth()) + "cm"   ; }
}
