from copy import copy
from ...Trap_parent import Traps

class Saw(Traps):

    def __init__(self, posIn, surface):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell = [1.5, 0, 64*1.5, 35*1.5]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 16

class Spike(Traps):

    def __init__(self, posIn, surface):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell = [0, 14, 64, 32]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 10