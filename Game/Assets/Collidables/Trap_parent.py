import pygame
from copy import copy
from abc import ABC


class Traps(ABC):
    """
    A parent class defining a trap

    Attributes
    ----------
    main_surface: pygame.Surface
        the main surface which will be drawn to

    Methods
    -------
    draw_traps():
        the method for drawing a trap onto the screen
    animation():
        the method from animating the trap
    update_animation(current_frame):
        a method which runs animation() in set intervals
    """

    def __init__(self, surface):
        """
        Constructs the necessary attributes for the trap

        Parameters
        ----------
        surface: pygame.Surface
            the main surface which will be drawn onto

        Returns
        -------
        None
        """

        self.main_surface = surface

    def draw_trap(self):
        """
        The method for drawing a trap

        Parameters
        ----------
        None

        Returns
        -------
        hitbox: pygame.Rect
            the rectangular hitbox of the trap
        """
        hitbox = self.main_surface.blit(self._animation, (self.posX, self.posY), self.shell)

        return hitbox

    def animation(self):
        """
        A method which increases the animation frame of the trap by 1.

        The method increments the animation frame by 1 each call and if the
        animation frame is the last one it resets to the beginning.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        if self.shell_phase <= self.max_phase - 1:
            self.shell_phase += 1
            self.shell[0] += self.shell[2]

        if self.shell_phase >= self.max_phase:
            self.shell_phase = 0
            self.shell = copy(self.def_shell)

    def update_animation(self, current_frame, framerate):
        """
        The method which updates the animation() in set intervals

        Parameters
        ----------
        current_frame: int
            the current frame which the program is on
        framerate: int
            the framerate which the trap runs at, separate from the program's framerate

        Returns
        -------
        None
        """
        if current_frame % framerate == 0:
            self.animation()