from classes import *

class Character:
    def __init__(self, name, sprite, inventory, posx, posy):
        self.name = name
        self.sprite = sprite
        self.health = 100
        self.inventory = inventory
        self.posx = posx
        self.posy = posy

    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getInventory(self):
        return self.inventory
    def getPosx(self):
        return self.posx
    def getPosy(self):
        return self.posy