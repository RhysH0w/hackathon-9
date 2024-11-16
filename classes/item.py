from classes import *

class Item():
    def __init__(self, name, itemType):
        self.name = name
        self.type = itemType
        
        self.description = ""

        if itemType not in ["wall", "weapon", "health", "sheild", "powered Arrow"] :
            print("Item not defined")



class Arrow():
    def __init__(self, effect):
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


    