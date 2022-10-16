public class Main {

    public static void clientCode(Subject subject){
        subject.request();
    }

    public static void main(String [] args){
        System.out.println("Client: Executing the client code with a real subject:");
        RealSubject realSubject = new RealSubject();
        clientCode(realSubject);

        System.out.println("Client: Executing the same client code with a proxy:");
        Proxy proxy = new Proxy(realSubject);
        clientCode(proxy);
    }
}
