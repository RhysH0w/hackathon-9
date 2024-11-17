<<<<<<< HEAD
from character import Character


class Enemy(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
=======
import sys
import os

# Add the project root directory to PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from classes.character import Character
from static.static import *

class Enemy(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
        #super().__init__(self, name, sprite, inventory, posx, posy)
        #The super() call automatically passes self to the Character class, so you don’t need to include self explicitly. 
>>>>>>> main
        super().__init__(name, sprite, inventory, posx, posy)
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
<<<<<<< HEAD
            if x >=0 and y >=0 and x < len(ownGrid):
                ownGrid[x][y] = value
        self._ownGrid = ownGrid
=======
            ownGrid[x][y] = value
        self._ownGrid = ownGrid
>>>>>>> main
