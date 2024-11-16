from classes.structures.specialBlock import specialBlock


class exitBlock(specialBlock):

        # Constructor

        def __init__(self, name, colour,):
            super().__init__(name, colour, "exit")
            _exitStatus = False

        # Getters

        def getExitStatus(self):
            return self._exitStatus

        # Setters

        def setExitStatus(self, exitStatus):
            self._exitStatus = exitStatus

        # Methods

        def toggle(self):
            return True