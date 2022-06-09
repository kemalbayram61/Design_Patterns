from Device    import Device
from Tablet    import Tablet
from Computer  import Computer
from Telephone import Telephone
from Mediator  import Mediator

if __name__ == "__main__":
    mediator: Mediator = Mediator()

    deviceList: list[Device] = []
    deviceList.append(Tablet(mediator))
    deviceList.append(Telephone(mediator))
    deviceList.append(Computer(mediator))

    for device in deviceList:
        device.runTest()