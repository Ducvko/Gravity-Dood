import os
from copy import copy
from ...Trap_parent import Traps

class Spear(Traps):

    def __init__(self, surface, posIn):
        super().__init__(surface)

        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell = [256, 0, 32, 130]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 4

class Tall_Saw(Traps):

    def __init__(self, surface):
        super().__init__(surface)