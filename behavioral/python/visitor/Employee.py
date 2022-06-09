from StaffVisitorA import StaffVisitor
from StaffA        import Staff

class Employee(Staff):
    def accept(self, staffVisitor: StaffVisitor) ->None:
        staffVisitor.visit(self)