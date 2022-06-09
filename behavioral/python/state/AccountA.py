from abc import ABC, abstractmethod
class AccountA(ABC):
    @abstractmethod
    def withdrawMoney(self, moneyAmount: int)-> None:
        pass
    @abstractmethod
    def depositMoney(self, moneyAmount: int)-> None:
        pass
    @abstractmethod
    def getAccountName(self)->str:
        pass
