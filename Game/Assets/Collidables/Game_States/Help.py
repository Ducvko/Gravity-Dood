import pygame
import os


class Help:
    """
    A class defining the title screen

    Attributes
    ----------
    surface: pygame.Surface
        the main surface which will be drawn on
    surfaceY: int
        the height of the window
    text: pygame.Surface
        the notification text
    button_sheet: pygame.Surface
        the spritesheet which the buttons are found on
    back_button: list
        the x, y, width, height of the back button found on the spritesheet

    Methods
    -------
    draw_elements():
        the method for drawing all elements of the help screen onto the main surface
    """

    def __init__(self, main_surface, surfaceY):
        """
        Constructs the necessary attributes for the help screen

        Parameters
        ----------
        main_surface: pygame.Surface
            the main surface which will be drawn on
        surfaceY: int
            the height of the window

        Returns
        -------
        None
        """

        self.surface = main_surface
        self.surfaceY = surfaceY

        font = pygame.font.SysFont(name='impact', size=35)

        self.text = font.render('The Instructions Are Displayed in Your Browser.', True, (230, 230, 230), None)

        buttons = pygame.image.load(os.path.join('Game', 'Assets', 'Collidables', 'Game_States', 'buttons.png'))
        self.button_sheet = pygame.transform.scale(buttons, (656 * 4, 128 * 4))
        self.back_button = [56 * 4, 41 * 4, 13 * 4, 15 * 4]

    def draw_element(self):
        """
        Draws all elements onto the help screen

        Parameters
        ----------
        None

        Returns
        -------
        back_hitbox: pygame.Rect
            the rectangular hitbox of the back button
        """

        self.surface.blit(self.text, (37, 30))

        back_hitbox = self.surface.blit(self.button_sheet, (0, self.surfaceY - 55), self.back_button)

        return back_hitbox