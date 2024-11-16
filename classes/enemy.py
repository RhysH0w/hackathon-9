from classes.character import Character
from static.static import *

class Enemy(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
        super().__init__(self, name, sprite, inventory, posx, posy)
        self._ownGrid = []
