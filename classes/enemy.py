from classes.character import Character

class Enemy(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
        super().__init__(self, name, sprite, inventory, posx, posy)