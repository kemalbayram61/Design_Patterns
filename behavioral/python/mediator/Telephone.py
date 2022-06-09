from Device   import Device

class Telephone(Device):

    def __init__(self, mediator):
        Device.__init__(self, mediator)
        self._mediator.setTelephone(self)

    def runTest(self) ->None:
        print("Telephone test started.")
        self._mediator.runTelephone()

    def endTest(self) ->None:
        print("Telephone test over.")