from AccountA   import AccountA
from TRYAccount import TRYAccount

class Account:
    __account: AccountA = None

    def __init__(self):
        self.__account = TRYAccount()

    def withdrawMoney(self, moneyAmount: int)->None:
        self.__account.withdrawMoney(moneyAmount)
    def depositMoney(self, moneyAmount: int)->None:
        self.__account.depositMoney(moneyAmount)
    def changeAccount(self, account:AccountA)->None:
        if(self.__account != None):
            print("Account change " + self.__account.getAccountName() + " to " + account.getAccountName())
        self.__account = account