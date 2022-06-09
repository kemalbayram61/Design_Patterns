from AccountA import AccountA

class EURAccount(AccountA):
    def withdrawMoney(self, moneyAmount: int) -> None:
        print("Withdraw money of EUR account. " + str(moneyAmount) + "EUR")
    def depositMoney(self, moneyAmount: int) -> None:
        print("Deposit money of EUR account. " + str(moneyAmount) + "EUR")
    def getAccountName(self) ->str:
        return "EUR"