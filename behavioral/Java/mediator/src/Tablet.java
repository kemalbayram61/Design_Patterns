public class Tablet extends Device{
    public Tablet(Mediator mediator) {
        super(mediator);
        this.mediator.setTablet(this);
    }

    @Override
    public void runTest() {
        System.out.println("Tablet test started.");
        this.mediator.runTablet();
    }

    @Override
    public void endTest() {
        System.out.println("Tablet test over.");
    }
}
