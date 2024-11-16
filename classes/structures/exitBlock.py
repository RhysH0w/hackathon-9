from classes.structures.block import Block


class exitBlock(Block):

        # Constructor

        def __init__(self, name, colour,):
            super().__init__(name, colour, "exit", True)
            _exitStatus = False

        # Getters

        def getExitStatus(self):
            return self._exitStatus

        # Setters

        def setExitStatus(self, exitStatus):
            self._exitStatus = exitStatus
