from abc import ABC, abstractmethod

class inventory_abstract(ABC):

    @abstractmethod
    def load_inventory(self) -> str:
        pass