from classes import *

class Character:
    def __init__(self, name, sprite, inventory, posx, posy):

        self._name = name
        self._sprite = sprite
        self._health = 100
        self._inventory = inventory
        self._position = posx, posy
        self.frozen = False
        self._visibleArea = []
        self._visionRange = 10

    def setVisibleArea(self, grid):
        visionRange = self._visionRange
        x, y = self._position
        visibleArea = []
        for i in range(max(0, x - visionRange), min(len(grid), x + visionRange + 1)):
            for j in range(max(0, y - visionRange), min(len(grid[0]), y + visionRange + 1)):
                visibleArea.append((i, j, grid[i][j]))
                # appends a tuple containing the x and y coordinates of  that particular square, and the kind of square
                # that that position is.
        self._visibleArea = visibleArea

    def moveCharacter(self, grid, move):
        x, y = self._position
        newX, newY = x + move[0], y + move[1]
        if 0 <= newX < len(grid) and 0 <= newY < len(grid[0]):
            self._position = newX, newY

    def getName(self):
        return self._name
    def getHealth(self):
        return self._health
    def getInventory(self):
        return self._inventory
    def getPosx(self):
        return self._posx
    def getPosy(self):
        return self._posy