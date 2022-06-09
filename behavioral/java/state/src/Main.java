public class Main {
    public static void main(String args[]){
        AccountA tryAccount = new TRYAccount();
        AccountA usdAccount = new USDAccount();
        AccountA eurAccount = new EURAccount();

        Account  account    = new Account();

        account.setAccount(tryAccount);
        account.depositMoney(50);
        account.withdrawMoney(50);

        account.setAccount(usdAccount);
        account.depositMoney(50);
        account.withdrawMoney(50);

        account.setAccount(eurAccount);
        account.depositMoney(50);
        account.withdrawMoney(50);
    }
}
