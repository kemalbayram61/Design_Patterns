import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String args[]){
        Mediator mediator       = new Mediator();
        List<Device> deviceList = new ArrayList<Device>();

        deviceList.add(new Telephone(mediator));
        deviceList.add(new Computer(mediator));
        deviceList.add(new Tablet(mediator));

        for(Device device: deviceList){
            device.runTest();
        }
    }
}
