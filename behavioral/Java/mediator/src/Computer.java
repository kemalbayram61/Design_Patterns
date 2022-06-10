public class Computer extends Device{
    public Computer(Mediator mediator) {
        super(mediator);
        this.mediator.setComputer(this);
    }

    @Override
    public void runTest() {
        System.out.println("Computer test started.");
        this.mediator.runComputer();
    }

    @Override
    public void endTest() {
        System.out.println("Computer test over.");
    }
}