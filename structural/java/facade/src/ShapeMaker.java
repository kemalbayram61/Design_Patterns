public class ShapeMaker {
    private Shape circle;
    private Shape rectangle;
    private Shape square;

    public ShapeMaker(){
        this.circle = new Circle();
        this.square = new Square();
        this.rectangle = new Rectangle();
    }

    public void drawCircle(){
        this.circle.draw();
    }

    public void drawRectangle(){
        this.rectangle.draw();
    }

    public void drawSquare(){
        this.square.draw();
    }
}
