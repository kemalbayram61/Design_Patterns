from AccountA import AccountA

class TRYAccount(AccountA):
    def withdrawMoney(self, moneyAmount: int) -> None:
        print("Withdraw money of TRY account. " + str(moneyAmount) + "TRY")
    def depositMoney(self, moneyAmount: int) -> None:
        print("Deposit money of TRY account. " + str(moneyAmount) + "TRY")
    def getAccountName(self) ->str:
        return "TRY"