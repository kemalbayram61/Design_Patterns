public class Telephone extends Device{
    public Telephone(Mediator mediator) {
        super(mediator);

    }

    @Override
    public void runTest() {
        System.out.println("Telephone test started.");
    }

    @Override
    public void endTest() {
        System.out.println("Telephone test over.");
    }
}
