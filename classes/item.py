from classes import *

class Item():
    def __init__(self, name, itemType):
        self.name = name
        self.type = itemType
        self.description = ""

        if itemType not in ["wall", "weapon", "health", "sheild", "powered Arrow"] :
            print("Item not defined")



class Arrow(Item):
    def __init__(self, effect):
        #super().__init__(self, "rrow", sprite, inventory, posx, posy)
        self.effect = effect

    def slow(self, player):
        try:
            player.freeze = True
        except Exception as e:
            print(e)

    def damage(self, player):
        try:
            player.health -= 20
        except Exception as e:
            print(e)

class Shield(Item):
    def __init__(self, shieldHealth):
        self.health = shieldHealth
    
    def useShield(self):
        self.health -= 10
        if self.health <= 0:
            return False
        return True
    
    def repairShield(self, amount):
        self.health += amount
        if self.health >= 100:
            return False
        return True
    