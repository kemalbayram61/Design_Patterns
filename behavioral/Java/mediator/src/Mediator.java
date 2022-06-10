public class Mediator {
    private Telephone telephone;
    private Tablet    tablet;
    private Computer  computer;

    public Telephone getTelephone() {
        return telephone;
    }

    public void setTelephone(Telephone telephone) {
        this.telephone = telephone;
    }

    public Tablet getTablet() {
        return tablet;
    }

    public void setTablet(Tablet tablet) {
        this.tablet = tablet;
    }

    public Computer getComputer() {
        return computer;
    }

    public void setComputer(Computer computer) {
        this.computer = computer;
    }

    public void runTelephone(){
        this.computer.endTest();
        this.tablet.endTest();
    }

    public void runTablet(){
        this.computer.endTest();
        this.telephone.endTest();
    }

    public void runComputer(){
        this.telephone.endTest();
        this.tablet.endTest();
    }
}
