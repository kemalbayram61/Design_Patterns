public class USDAccount implements AccountA{
    @Override
    public void withdrawMoney(int moneyAmount) {
        System.out.println("Withdraw money of USD account. " + Integer.toString(moneyAmount) + "USD");
    }

    @Override
    public void depositMoney(int moneyAmount) {
        System.out.println("Deposit money of USD account. " + Integer.toString(moneyAmount) + "USD");
    }

    @Override
    public String getAccountName() {
        return "USD";
    }
}
