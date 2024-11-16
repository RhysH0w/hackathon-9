from classes.structures.block import Block

class doorBlock(Block):

        # Constructor

        def __init__(self, name, colour, passthrough):
            super().__init__(name, colour, "door", passthrough)

        # Getters

        def getPassThrough(self):
            return self._passThrough

        # Methods

        def toggle(self):
            if self._passThrough:
                self._passThrough = False
            else:
                self._passThrough = True


