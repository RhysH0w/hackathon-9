from classes import *

class Item:
    def __init__(self, name, itemType):
        self.name = name
        self.type = itemType
        
        self.description = ""

        if itemType not in ["wall", "weapon", "health", "sheild"] :
            print("Item not defined")



class 

    