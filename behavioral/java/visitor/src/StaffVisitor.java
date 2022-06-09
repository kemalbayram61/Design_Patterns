public interface StaffVisitor {
    void visit(Employee employee);
    void visit(Manager manager);
}
