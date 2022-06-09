from StaffA        import Staff
from StaffVisitorA import StaffVisitor

class SalaryCalculationVisitor(StaffVisitor):
    def visit(self, staff: Staff) ->None:
        if(str(type(staff)) == "<class 'Employee.Employee'>"):
            print("Employee salary calculated.")
        elif(str(type(staff)) == "<class 'Manager.Manager'>"):
            print("Manager salary calculated.")