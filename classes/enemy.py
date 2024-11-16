from classes.character import Character
from static.static import *

class Enemy(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
        super().__init__(self, name, sprite, inventory, posx, posy)
        self._ownGrid = []

    def buildFirstGrid(self, grid):
        ownGrid = []
        for i in range (len(grid)):
            ownGrid.append([])
            for j in range (len(grid[0])):
                ownGrid[i].append(-1)

    def updateOwnGrid(self):
        ownGrid = self._ownGrid
        visibleArea = self._visibleArea
        for x, y, value in visibleArea:
            ownGrid[x][y] = value
        self._ownGrid = ownGrid