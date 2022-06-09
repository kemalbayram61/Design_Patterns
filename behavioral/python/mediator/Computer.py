from Device   import Device

class Computer(Device):

    def __init__(self, mediator):
        Device.__init__(self, mediator)
        self._mediator.setComputer(self)

    def runTest(self) ->None:
        print("Computer test started.")
        self._mediator.runComputer()

    def endTest(self) ->None:
        print("Computer test over.")