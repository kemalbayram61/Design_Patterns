from AccountA   import AccountA
from TRYAccount import TRYAccount
from USDAccount import USDAccount
from EURAccount import EURAccount
from Account    import Account

if __name__ == "__main__":
    usdAccount: AccountA = USDAccount()
    eurAccount: AccountA = EURAccount()
    tryAccount: AccountA = TRYAccount()

    account: Account = Account()
    account.changeAccount(usdAccount)
    account.withdrawMoney(50)
    account.depositMoney(50)

    account.changeAccount(eurAccount)
    account.withdrawMoney(50)
    account.depositMoney(50)

    account.changeAccount(tryAccount)
    account.withdrawMoney(50)
    account.depositMoney(50)