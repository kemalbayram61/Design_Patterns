public abstract class Device {

    protected Mediator mediator;

    public Device(Mediator mediator){
        this.mediator = mediator;
    }

    public abstract void runTest();

    public abstract void endTest();
}
