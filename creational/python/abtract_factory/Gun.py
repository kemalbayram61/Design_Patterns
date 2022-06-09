from InventoryA import inventory_abstract

class gun(inventory_abstract):

    def load_inventory(self) -> str:
        return "Invntory gun is loaded."