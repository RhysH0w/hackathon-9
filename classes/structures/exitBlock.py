from classes.structures.specialBlock import specialBlock


class exitBlock(specialBlock):

        # Constructor

        def __init__(self, name, colour, type):
            super().__init__(name, colour, type)

        # Methods

        def toggle(self):
            return True