import os
import pygame


class Short:

    def __init__(self, posIn):
        self.posX = posIn[0]
        self.posY = posIn[1]
        
        self.spike_rate = 7
        self.saw_rate = 7
        self.acid_rate = 7

        self.saw = pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Saw Trap - Level 1.png"))
        self.spike = pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Spike_B.png"))
        self.acid = pygame.image.load(os.path.join("Game\Assets\Collidables\Static\Short", "Toxic Trap - Level 1.png"))