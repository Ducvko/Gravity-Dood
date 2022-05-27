import pygame
import os
from copy import copy
from abc import ABC


class Traps(ABC):

    def __init__(self, surface):
        self.main_surface = surface
        
        self.spike_rate = 8
        self.saw_rate = 5
        self.spear_rate = 15

        self.animations = [pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Saw Trap - Level 1.png")),            # Saw Spritesheet
                           pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Spike_B.png")),                       # Spike Spritesheet
                           pygame.image.load(os.path.join("Game", "Assets", "Collidables", "Static", "Tall", "Saw Trap - Level 2.png")), # Tall Saw spritesheet
                           pygame.image.load(os.path.join("Game", "Assets", "Collidables", "Static", "Tall", "Spear.png"))]              # Spear Spritesheet

        for i in range(4):
            self.animations[i] = pygame.transform.scale2x(self.animations[i])

    def draw_trap(self, animation, posX, posY):
        self.main_surface.blit(self.animations[animation], (posX, posY), self.shell)

    def animation(self):
        if self.shell_phase <= self.max_phase - 1:
            self.shell_phase += 1
            self.shell[0] += self.shell[2]

        if self.shell_phase >= self.max_phase:
            self.shell_phase = 0
            self.shell = copy(self.def_shell)

    def update_animation(self, current_frame, framerate):
        if current_frame % framerate == 0:
            self.animation()