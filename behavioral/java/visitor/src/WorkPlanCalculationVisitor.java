public class WorkPlanCalculationVisitor implements StaffVisitor{

    @Override
    public void visit(Employee employee) {
        System.out.println("Employee work plan calculated.");
    }

    @Override
    public void visit(Manager manager) {
        System.out.println("Manager work plan calculated.");
    }
}
