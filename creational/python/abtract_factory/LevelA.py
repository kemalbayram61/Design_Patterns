from abc        import ABC, abstractmethod
from EnemyA     import enemy_abstract
from InventoryA import inventory_abstract

class level_abtract(ABC):

    @abstractmethod
    def create_enemy(self)-> enemy_abstract:
        pass

    @abstractmethod
    def create_inventory(self)-> inventory_abstract:
        pass