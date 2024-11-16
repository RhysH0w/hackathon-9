class groundBlock:

    # Constructor
    def __init__(self, name, colour):
        self._name = name
        self._colour = colour


    # Getters

    def getName(self):
        return self._name

    def getColour(self):
        return self._colour

    # Setters

    def setName(self, name):
        self._name = name

    def setColour(self, colour):
        self._colour = colour

