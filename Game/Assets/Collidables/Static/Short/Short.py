import pygame
import os
from copy import copy
from ...Trap_parent import Traps

class Saw(Traps):

    def __init__(self, posIn, surface):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.animation = pygame.transform.scale(pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Saw Trap - Level 1.png")), (1024*1.5, 64*1.5))

        self.shell = [1.5, 0, 64*1.5, 35*1.5]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 16

        self.framerate = 5

class Spike(Traps):

    def __init__(self, posIn, surface):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.animation = pygame.transform.scale2x(pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Spike_B.png")))

        self.shell = [0, 14, 64, 32]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 10

        self.framerate = 8