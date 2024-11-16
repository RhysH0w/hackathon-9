from classes import *

class Item():
    def __init__(self, name, itemType, description):
        self.name = name
        self.type = itemType
        self.health = 100
        self.description = description

        if itemType not in ["wall", "weapon", "health", "sheild", "powered Arrow"] :
            print("Item not defined")

    def useItem(self):
        self.health -= 10
        if self.health <= 0:
            return False
        return True
    
    def repairItem(self, amount):
        self.health += amount
        if self.health >= 100:
            return False
        return True



class Arrow(Item):
    def __init__(self, effect):
        description = "A weapon that can be used to slow or attack"
        super().__init__(self, effect+" arrow", 'Arrow', description)
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
        description = "A tool that can be used to defend attacks"
        super().__init__(self, f"Shield ({shieldHealth})", 'Shield', description)
        self.health = shieldHealth

class Torch(Item):
    def __init__(self, batteryLevel):
        description = "A tool that can be used to view a larger area"
        super().__init__(self, f"Torch ({batteryLevel})", 'Torch', description)
        self.health = batteryLevel