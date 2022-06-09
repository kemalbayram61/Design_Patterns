public class Account {
    private AccountA account;
    public Account(){
        this.account = null;
    }
    public void setAccount(AccountA account){
        if(this.account != null)
            System.out.println("Account change " + this.account.getAccountName() + " to " + account.getAccountName());
        else
            System.out.println("Select " + account.getAccountName() + " account.");
        this.account = account;
    }
    public void withdrawMoney(int moneyAmount) {
        if(this.account != null)
            this.account.withdrawMoney(moneyAmount);
    }

    public void depositMoney(int moneyAmount) {
        if(this.account != null)
            this.account.depositMoney(moneyAmount);
    }
}
