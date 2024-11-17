import sys
import os

# Add the project root directory to PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from classes.character import Character


class Player(Character):
    def __init__(self, name, sprite, inventory, posx, posy):
        #super().__init__(self, name, sprite, inventory, posx, posy)
        #The super() call automatically passes self to the Character class, so you don’t need to include self explicitly. 
        super().__init__(name, sprite, inventory, posx, posy)