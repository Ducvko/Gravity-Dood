import os
import pygame
from abc import ABC


class Short(ABC):

    def __init__(self, surface):
        self.main_surface = surface
        
        self.spike_rate = 7
        self.saw_rate = 7
        self.acid_rate = 7

        self.animations = [pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Saw Trap - Level 1.png")),   # Saw Spritesheet
                           pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Spike_B.png")),              # Spike Spritesheet
                           pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Toxic Trap - Level 1.png"))] # Acid Spritesheet

    def draw_trap(self, animation):
        self.main_surface.blit(self.animations[animation], self.main_surface, self.shell)

class Saw(Short):

    def __init__(self, posIn, surface):
        super.__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell

        self.shell_phase = 0
        self.max_phase = 9


class Spike(Short):

    def __init__(self, posIn, surface):
        super.__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell

class Acid(Short):

    def __init__(self, posIn, surface):
        super.__init__(surface)
        self.posX = posIn[0]
        self.posY = posIn[1]

        self.shell