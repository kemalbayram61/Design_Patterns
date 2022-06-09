public class Main
{
    public static void main(String[] args)
    {
        Employee employee = new Employee();
        Manager  manager  = new Manager();

        SalaryCalculationVisitor   scv  = new SalaryCalculationVisitor();
        WorkPlanCalculationVisitor wpcv = new WorkPlanCalculationVisitor();

        employee.accept(scv);
        employee.accept(wpcv);

        manager.accept(scv);
        manager.accept(wpcv);
    }
}
