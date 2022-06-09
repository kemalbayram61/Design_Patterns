public class Employee implements Staff{
    @Override
    public void accept(StaffVisitor staffVisitor) {
        staffVisitor.visit(this);
    }
}
