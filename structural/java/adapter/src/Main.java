public class Main {
    public  static  void main(String[] args) {
        Rectangle rectangle = new Rectangle(10, 20);
        rectangle.draw();
        System.out.println("###########################################################");
        RectangleToTriangleAdapter adapter = new RectangleToTriangleAdapter(rectangle);
        adapter.draw();
    }
}
