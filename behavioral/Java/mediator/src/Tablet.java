public class Tablet extends Device{
    public Tablet(Mediator mediator) {
        super(mediator);

    }

    @Override
    public void runTest() {
        System.out.println("Tablet test started.");
    }

    @Override
    public void endTest() {
        System.out.println("Tablet test over.");
    }
}
