class Block:

    # Constructor
    def __init__(self, name, colour, type, passThrough):
        self._name = name
        self._colour = colour
        self._type = type
        self._passThrough = passThrough


    # Getters

    def getName(self):
        return self._name

    def getColour(self):
        return self._colour

    def getType(self):
        return self._type

    def getPassThrough(self):
        return self._passThrough

    # Setters

    def setName(self, name):
        self._name = name

    def setColour(self, colour):
        self._colour = colour

    def setType(self, type):
        self._type = type

    def setPassThrough(self, passThrough):
        self._passThrough = passThrough

