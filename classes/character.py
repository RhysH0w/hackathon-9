class Character:
    def __init__(self, name, sprite, inventory):
        self.name = name
        self.sprite = sprite
        self.health = 100
        self.inventory = inventory

    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getInventory(self):
        return self.inventory