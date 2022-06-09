from python.abtract_factory.levelDesigner import *

class game_creator:
    level_number = None

    def __init__(self, level_number):
        self.level_number = level_number

    def get_game(self):
        if(self.level_number == 1):
            return  level_1()
        elif(self.level_number == 2):
            return  level_2()