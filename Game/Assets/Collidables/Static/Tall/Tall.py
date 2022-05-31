import pygame
import os
from copy import copy
from ...Trap_parent import Traps

class Spear(Traps):

    def __init__(self, surface, posIn):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        spritesheet = pygame.image.load(os.path.join("Game", "Assets", "Collidables", "Static", "Tall", "Spear.png"))
        self._animation = pygame.transform.scale2x(spritesheet)

        self.shell = [256, 0, 32, 130]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 4

        self.framerate = 15

class Tall_Saw(Traps):

    def __init__(self, surface, posIn):
        super().__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        spritesheet = pygame.image.load(os.path.join("Game", "Assets", "Collidables", "Static", "Tall", "Saw Trap - Level 2.png"))
        self._animation = pygame.transform.scale2x(spritesheet)

        self.shell = [2, 0, 128, 130]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 30

        self.framerate = 5