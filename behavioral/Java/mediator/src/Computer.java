public class Computer extends Device{
    public Computer(Mediator mediator) {
        super(mediator);

    }

    @Override
    public void runTest() {
        System.out.println("Computer test started.");
    }

    @Override
    public void endTest() {
        System.out.println("Computer test over.");
    }
}