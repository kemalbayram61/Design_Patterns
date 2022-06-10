public class RectangleToTriangleAdapter implements Shape{

    private double width;
    private double height;
    private Rectangle rectangle;
    private Triangle triangle;
    public RectangleToTriangleAdapter(Rectangle rectangle){
        this.rectangle = rectangle;
        this.triangle  = new Triangle(this.rectangle.getWidth(), this.rectangle.getHeight());
    }
    @Override
    public void draw() {
        this.triangle.draw();
    }

    @Override
    public double getWidth() {
        return this.width;
    }

    @Override
    public double getHeight() {
        return this.height;
    }
}
