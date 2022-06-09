public class TRYAccount implements AccountA{
    @Override
    public void withdrawMoney(int moneyAmount) {
        System.out.println("Withdraw money of TRY account. " + Integer.toString(moneyAmount) + "TRY");
    }

    @Override
    public void depositMoney(int moneyAmount) {
        System.out.println("Deposit money of TRY account. " + Integer.toString(moneyAmount) + "TRY");
    }

    @Override
    public String getAccountName() {
        return "TRY";
    }
}
