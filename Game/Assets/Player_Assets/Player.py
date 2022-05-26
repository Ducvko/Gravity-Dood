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

        self.animations = pygame.transform.scale(self.animations, (385*3, 592*3))
        
        self.shell = [54, 44, 50, 30]
                    # x, y, width, height
        
        for i in range(len(self.shell)):
            self.shell[i] = self.shell[i]*3

        self.def_shell = copy(self.shell)

        self.shell_phase = 0
        self.max_phase = 6     
        self.player_rate = 6

        self.speed = speed
        self.upside_down = False

    def draw_player(self):

        hitbox = pygame.Surface((self.shell[2], self.shell[3]))
        hitbox.set_colorkey((0,0,0))

        hitbox.blit(self.animations, (0, 0), self.shell)

        if self.upside_down:
            hitbox = pygame.transform.flip(hitbox, False, True)

        self.main_surface.blit(hitbox, (self.posX, self.posY))   

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
        