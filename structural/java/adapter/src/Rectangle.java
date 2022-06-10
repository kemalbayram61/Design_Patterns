public class Rectangle implements Shape{
    private double width;
    private double height;

    public Rectangle(double width, double height){
        this.width  = width;
        this.height = height;
    }
    @Override
    public void draw() {
        for(int i=0;i<this.height; i++){
            for(int j=0; j<this.width; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
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
