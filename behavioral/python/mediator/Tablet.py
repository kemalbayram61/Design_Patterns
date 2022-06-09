from Device   import Device

class Tablet(Device):

    def __init__(self, mediator):
        Device.__init__(self, mediator)
        self._mediator.setTablet(self)

    def runTest(self) ->None:
        print("Tablet test started.")
        self._mediator.runTablet()

    def endTest(self) ->None:
        print("Tablet test over.")