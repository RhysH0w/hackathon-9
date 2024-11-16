from classes.character import Character


class Player(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
        super().__init__(self, name, sprite, inventory, posx, posy)