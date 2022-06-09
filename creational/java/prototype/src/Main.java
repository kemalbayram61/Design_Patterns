public class Main
{
    public static void main(String[] args)
    {
        Coordinate coordinate = new Coordinate();

        coordinate.setX(1);
        coordinate.setY(2);
        coordinate.setZ(3);

        Coordinate coordinateCopy = coordinate.getCoordinateCopy();

        System.out.println(coordinateCopy.getX());

        coordinateCopy.setX(5);

        System.out.println(coordinate.getX());

        System.out.println(coordinateCopy.getX());
    }
}
