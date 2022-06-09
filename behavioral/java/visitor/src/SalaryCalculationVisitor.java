public class SalaryCalculationVisitor implements StaffVisitor{
    @Override
    public void visit(Employee employee) {
        System.out.println("Employee salary calculated.");
    }

    @Override
    public void visit(Manager manager) {
        System.out.println("Manager salary calculated.");
    }
}
