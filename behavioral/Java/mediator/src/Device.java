public abstract class Device {

    //TODO: mediator type update
    protected String mediator;

    public Device(String mediator){
        this.mediator = mediator;
    }

    public abstract void runTest();

    public abstract void endTest();
}
