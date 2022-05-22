import pygame
import os
from copy import copy

class Player:

    def __init__(self, posIn, surface, surface_dimensions: list, speed):
        self.posX = posIn[0]
        self.posY = posIn[1]
        self.main_surface = surface
        self.surfaceX = surface_dimensions[0]
        self.surfaceY = surface_dimensions[1]

        self.animations = pygame.image.load(os.path.join("Game\Assets\Player_Assets\Animations", "adventurer-v1.5-Sheet.png"))

        self.shell = [54, 44, 50, 30]
                     # x, y, width, height
        self.def_shell = copy(self.shell)

        self.shell_phase = 0
        self.max_phase = 6     
        self.player_rate = 6
        self.speed = speed

    def draw_player(self):

        self.main_surface.blit(self.animations, (self.posX, self.posY), self.shell)
        

    def player_run(self):

        if self.shell_phase <= self.max_phase - 1:
            self.shell_phase += 1
            self.shell[0] += self.shell[2]

        if self.shell_phase >= self.max_phase:
            self.shell_phase = 0
            self.shell = copy(self.def_shell)

    def frame_update(self, current_frame):
        if current_frame % self.player_rate == 0:
            self.player_run()
        