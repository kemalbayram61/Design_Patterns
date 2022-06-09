from python.abtract_factory.gameCreator import game_creator

if __name__ == "__main__":
    level_1 = game_creator(1).get_game()
    level_2 = game_creator(2).get_game()

    enemy     = level_1.create_enemy()
    inventory = level_1.create_inventory()

    print(enemy.place_enemy())
    print(inventory.load_inventory())
    print("Game ready for start.")