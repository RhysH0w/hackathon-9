from classes.structures.specialBlock import specialBlock


class doorBlock(specialBlock):

        # Constructor

        def __init__(self, name, colour, locked):
            super().__init__(name, colour, "door")
            self._locked = locked

        # Getters

        def isLocked(self):
            return self._locked

        # Setters

        def toggle(self):
            self._locked = not self._locked
            return self._locked


