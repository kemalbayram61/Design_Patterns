from abc import ABC, abstractmethod

class enemy_abstract(ABC):

    @abstractmethod
    def place_enemy(self) -> str:
        pass