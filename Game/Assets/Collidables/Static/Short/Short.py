import pygame
import os
from copy import copy
from ...Trap_parent import Traps


class Saw(Traps):
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

    def __init__(self, posIn, surface):
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

        spritesheet = pygame.image.load(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Assets', 'Collidables', 'Static', 'Short', "Saw Trap - Level 1.png"))
        self._animation = pygame.transform.scale(spritesheet, (1024*1.5, 64*1.5))

        self.shell = [1.5, 0, 64*1.5, 35*1.5]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 16

        self.framerate = 5

class Spike(Traps):
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

    def __init__(self, posIn, surface):
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

        spritesheet = pygame.image.load(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Assets', 'Collidables', 'Static', 'Short', "Spike_B.png"))
        self._animation = pygame.transform.scale2x(spritesheet)

        self.shell = [0, 14, 64, 32]
        self.def_shell = copy(self.shell)

        self.shell_phase = 1
        self.max_phase = 10

        self.framerate = 8