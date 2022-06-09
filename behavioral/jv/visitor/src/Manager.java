public class Manager implements Staff{
    @Override
    public void accept(StaffVisitor staffVisitor) {
        staffVisitor.visit(this);
    }
}
