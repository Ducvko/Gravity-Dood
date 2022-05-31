import pygame
import os
from copy import copy
from abc import ABC


class Traps(ABC):

    def __init__(self, surface):
        self.main_surface = surface

    def draw_trap(self):
        self.main_surface.blit(self._animation, (self.posX, self.posY), self.shell)

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