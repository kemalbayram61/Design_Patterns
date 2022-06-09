from AccountA import AccountA

class USDAccount(AccountA):
    def withdrawMoney(self, moneyAmount: int) -> None:
        print("Withdraw money of USD account. " + str(moneyAmount) + "USD")
    def depositMoney(self, moneyAmount: int) -> None:
        print("Deposit money of USD account. " + str(moneyAmount) + "USD")
    def getAccountName(self) ->str:
        return "USD"