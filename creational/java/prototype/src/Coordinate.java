public class Coordinate implements Cloneable
{
    private double x;
    private double y;
    private double z;

    protected Coordinate getCoordinateCopy()
    {
        try
        {
            return (Coordinate) super.clone();
        }
        catch (CloneNotSupportedException e)
        {
            e.printStackTrace();
            return null;
        }
    }

    public double getX() {
        return x;
    }

    public void setX(double x) {
        this.x = x;
    }

    public double getY() {
        return y;
    }

    public void setY(double y) {
        this.y = y;
    }

    public double getZ() {
        return z;
    }

    public void setZ(double z) {
        this.z = z;
    }
}
