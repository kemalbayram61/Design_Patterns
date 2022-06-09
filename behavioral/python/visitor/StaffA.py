from abc           import ABC, abstractmethod
from StaffVisitorA import StaffVisitor
class Staff(ABC):
    @abstractmethod
    def accept(self, staffVisitor)->None:
        pass