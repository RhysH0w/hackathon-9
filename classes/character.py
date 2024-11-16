from classes import *

class Character:
    def __init__(self, name, sprite, inventory, posx, posy):
        self.name = name
        self.sprite = sprite
        self.health = 100
        self.inventory = inventory
        self.position = posx, posy

    def getVisibleArea(self, grid, visionRange):
        x, y = self.position
        visibleArea = []
        for i in range(max(0, x - visionRange), min(len(grid), x + visionRange + 1)):
            for j in range(max(0, y - visionRange), min(len(grid[0]), y + visionRange + 1)):
                visibleArea.append((i, j, grid[i][j]))
        return visibleArea

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