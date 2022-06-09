from StaffA        import Staff
from StaffVisitorA import StaffVisitor

class WorkPlanCalculationVisitor(StaffVisitor):
    def visit(self, staff: Staff) ->None:
        if(str(type(staff)) == "<class 'Employee.Employee'>"):
            print("Employee work plan calculated.")
        elif(str(type(staff)) == "<class 'Manager.Manager'>"):
            print("Manager work plan calculated.")