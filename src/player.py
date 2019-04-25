# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, currentroom, hunger=0):
        self.name = name
        self.currentroom = currentroom
        self.inventory = []
        self.hunger = hunger

    def move_to(self, direction):
        pass

    def add_inventory(self, item):
        self.inventory.append(item)
