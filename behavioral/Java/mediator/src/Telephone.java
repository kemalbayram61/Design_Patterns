public class Telephone extends Device{
    public Telephone(Mediator mediator) {
        super(mediator);
        this.mediator.setTelephone(this);
    }

    @Override
    public void runTest() {
        System.out.println("Telephone test started.");
        this.mediator.runTelephone();
    }

    @Override
    public void endTest() {
        System.out.println("Telephone test over.");
    }
}
