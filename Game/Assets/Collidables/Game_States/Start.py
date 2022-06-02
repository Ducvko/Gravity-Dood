import os
import pygame


class Title:
    """
    A class defining the title screen

    Attributes
    ----------
    surface: pygame.Surface
        the main surface which will be drawn on
    title: pygame.Surface
        the title text of the game
    button_sheet: pygame.Surface
        the spritesheet which the buttons are found on
    start_button: list
        the x, y, width, height of the start button found on the spritesheet
    credits_button: list
        the x, y, width, height of the credits button found on the spritesheet

    Methods
    -------
    draw_elements():
        the method for drawing all elements of the title screen onto the main surface
    """

    def __init__(self, main_surface):
        """
        Constructs the necessary attributes of the title screen

        Parameters
        ----------
        main_surface: pygame.Surface
            the main surface which will be drawn on

        Returns
        -------
        None
        """
        self.surface = main_surface

        title_font = pygame.font.SysFont(name='impact', size=42)

        self.title = title_font.render('GRAVITY DOOD', True, (230, 230, 230), None)

        buttons = pygame.image.load(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Assets', 'Collidables', 'Game_States', 'buttons.png'))
        self.button_sheet = pygame.transform.scale2x(buttons)
        self.start_button = [384 * 2, 1 * 2, 64 * 2, 30 * 2]
        self.credits_button = [448 * 2, 1 * 2, 80 * 2, 30 * 2]

    def draw_elements(self):
        """
        The method for drawing all elements onto the title screen

        Parameters
        ----------
        None

        Returns
        -------
        start_hitbox: pygame.Rect
            the hitbox for the start button
        credits_hitbox: pygame.Rect
            the hitbox for the credits button
        """

        self.surface.blit(self.title, (255, 0))

        start_hitbox = self.surface.blit(self.button_sheet, (310, 130), self.start_button)

        credits_hitbox = self.surface.blit(self.button_sheet, (295, 190), self.credits_button)

        return start_hitbox, credits_hitbox


