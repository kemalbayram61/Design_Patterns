public class EURAccount implements AccountA{
    @Override
    public void withdrawMoney(int moneyAmount) {
        System.out.println("Withdraw money of EUR account. " + Integer.toString(moneyAmount) + "EUR");
    }

    @Override
    public void depositMoney(int moneyAmount) {
        System.out.println("Deposit money of EUR account. " + Integer.toString(moneyAmount) + "EUR");
    }

    @Override
    public String getAccountName() {
        return "EUR";
    }
}
