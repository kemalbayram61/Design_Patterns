public class Triangle implements Shape{
    private double width;
    private double height;
    public Triangle(double width, double height){
        this.width  = width;
        this.height = height;
    }
    @Override
    public void draw() {
        int width = 1;
        for(int i=0;i<this.height; i++){
            for(int j=0; j<(this.height - width); j++) {
                System.out.print(" ");
            }
            for(int j=0; j<width * 2; j++) {
                System.out.print("*");
            }
            width = width + 1;
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
