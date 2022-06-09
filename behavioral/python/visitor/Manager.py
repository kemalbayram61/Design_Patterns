from StaffA import Staff
from StaffVisitorA import StaffVisitor

class Manager(Staff):
    def accept(self, staffVisitor: StaffVisitor) ->None:
        staffVisitor.visit(self)