import pygame
import os

class Player:

    def __init__(self, posIn: list, surface, surface_dimensions: list, speed):
        self.posX = posIn[0]
        self.posY = posIn[1]
        self.main_surface = surface
        self.surfaceX = surface_dimensions[0]
        self.surfaceY = surface_dimensions[1]

        self.animations = pygame.image.load(os.path.join("Player_Assets/Animations", "adventurer-v1.5-Sheet.png"))

        self.shell = [54, 42, 15, 33]
                     # x, y, width, height
        self.speed = speed

    def gravity(self):


    def player_run(self):
        shell_phase = 0
        max_phase = 6

        if shell_phase < max_phase - 1:
            shell_phase += 1
            self.shell[0] += self.shell[2]

        elif shell_phase >= max_phase:
            shell_phase = 0
            self.shell[0] -= self.shell[2] * (max_phase - 1)
        
        self.main_surface.blit(self.animations, (self.surfaceX // 2, self.surfaceY // 2), self.shell)