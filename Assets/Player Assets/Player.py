from typing import Iterable
import pygame

class Player:

    def __init__(self, posIn: list, surface, surface_dimensions: list, speed):
        self.posX = posIn[0]
        self.posY = posIn[1]
        self.main_surface = surface
        self.surfaceX = surface_dimensions[0]
        self.surfaceY = surface_dimensions[1]

        self.speed = speed