public class Proxy implements Subject{
    private RealSubject realSubject;

    public Proxy(RealSubject realSubject){
        this.realSubject = realSubject;
    }

    @Override
    public void request() {
        if(this.checkAccess()){
            this.realSubject.request();
            this.logAccess();
        }
    }

    public boolean checkAccess(){
        System.out.println("Proxy: Checking access prior to firing a real request.");
        return true;
    }

    public void logAccess(){
        System.out.println("Proxy: Logging the time of request.");
    }
}
