import pygame
import os
from copy import copy
from ...Trap_parent import Traps


class Spear(Traps):
    """
    A child class which defines a spear, inherits from the Traps class

    Attributes
    ----------
    posX: int
        the x position of the trap
    posY: int
        the y position of the trap
    _animation: pygame.Surface
        the spritesheet of the trap
    shell: list
        a list containing the x, y, width, and height of the trap frame on the spritesheet
    def_shell: list
        a copy of the default shell values
    shell_phase: int
        the starting frame of the animation
    max_phase: int
        the ending frame of the animation
    framerate: int
        the framerate which the trap animates at, seperate from the program's framerate

    Methods
    -------
    None
    """

    def __init__(self, surface, posIn):
        """
        Constructs the necessary attributes of the trap

        Parameters
        ----------
        surface: pygame.Surface
            the main surface which will be drawn on
        posIn: list
            the x, y positions of the trap

        Returns
        -------
        None
        """

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
    """
    A child class which defines a spear, inherits from the Traps class

    Attributes
    ----------
    posX: int
        the x position of the trap
    posY: int
        the y position of the trap
    _animation: pygame.Surface
        the spritesheet of the trap
    shell: list
        a list containing the x, y, width, and height of the trap frame on the spritesheet
    def_shell: list
        a copy of the default shell values
    shell_phase: int
        the starting frame of the animation
    max_phase: int
        the ending frame of the animation
    framerate: int
        the framerate which the trap animates at, seperate from the program's framerate

    Methods
    -------
    None
    """

    def __init__(self, surface, posIn):
        """
        Constructs the necessary attributes of the trap

        Parameters
        ----------
        surface: pygame.Surface
            the main surface which will be drawn on
        posIn: list
            the x, y positions of the trap

        Returns
        -------
        None
        """

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