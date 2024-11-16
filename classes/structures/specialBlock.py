class specialBlock:

    # Constructor

    def __init__(self, name, colour, type):
        self._name = name
        self._colour = colour
        self._type = type


    # Getters

    def getName(self):
        return self._name

    def getColour(self):
        return self._colour

    def getType(self):
        return self._type

    # Setters

    def setName(self, name):
        self._name = name

    def setColour(self, colour):
        self._colour = colour

    def setType(self, type):
        self._type = type

    # Methods
    def toggle(self):
        return False
