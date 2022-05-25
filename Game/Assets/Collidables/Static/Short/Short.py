from copy import copy
import os
import pygame
from ...Trap_parent import Traps

class Saw(Traps):

    def __init__(self, posIn, surface):
        super.__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell



class Spike(Traps):

    def __init__(self, posIn, surface):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell = [0, 7, 32, 16]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 10