from LevelA     import level_abtract
from InventoryA import inventory_abstract
from EnemyA     import enemy_abstract
from Spider     import spider
from Slign      import slign
from Robot      import robot
from Gun        import gun

class level_1(level_abtract):

    def create_inventory(self) -> inventory_abstract:
        return slign()

    def create_enemy(self) -> enemy_abstract:
        return  spider()

class level_2(level_abtract):

    def create_enemy(self) -> enemy_abstract:
        return  robot()

    def create_inventory(self) -> inventory_abstract:
        return  gun()