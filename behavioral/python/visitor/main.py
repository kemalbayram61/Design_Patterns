from WorkPlanCalculationVisitor import WorkPlanCalculationVisitor
from SalaryCalculationVisitor   import SalaryCalculationVisitor
from Employee                   import Employee
from Manager                    import Manager

if __name__ == "__main__":
    employee: Employee = Employee()
    manager : Manager  = Manager()

    salaryCalculationVisitor  : SalaryCalculationVisitor   = SalaryCalculationVisitor()
    workPlanCalculationVisitor: WorkPlanCalculationVisitor = WorkPlanCalculationVisitor()

    employee.accept(salaryCalculationVisitor)
    employee.accept(workPlanCalculationVisitor)

    manager.accept(salaryCalculationVisitor)
    manager.accept(workPlanCalculationVisitor)