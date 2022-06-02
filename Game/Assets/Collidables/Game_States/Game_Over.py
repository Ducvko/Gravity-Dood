import pygame
import os


class GameOver:
    """
    A class defining the title screen

    Attributes
    ----------
    surface: pygame.Surface
        the main surface which will be drawn on
    game_over: pygame.Surface
        the game over text
    score_font: pygame.font
        the font used for the highscore and score
    button_sheet: pygame.Surface
        the spritesheet which the buttons are found on
    quit_button: list
        the x, y, width, height of the quit button found on the spritesheet
    menu_button: list
        the x, y, width, height of the menu button found on the spritesheet
    restart_button: list
        the x, y, width, height of the restart button found on the spritesheet

    Methods
    -------
    draw_elements(scoreIn, highscore):
        the method for drawing all elements of the game over screen onto the main surface
    """

    def __init__(self, main_surface):
        """
        Constructs all necessary attributes of the game over screen

        Parameters
        ----------
        main_surface: pygame.Surface
            the main surface which will be drawn on

        Returns
        -------
        None
        """

        self.surface = main_surface

        font = pygame.font.SysFont(name='impact', size=50)

        self.game_over = font.render('GAME OVER!', True, (230, 230, 230), None)

        self.score_font = pygame.font.SysFont(name='trebuchetms', size=35)

        buttons = pygame.image.load(os.getcwd().replace("\\dist\\Gravity_Dood", "") + "\\" + os.path.join('Assets', 'Collidables', 'Game_States', 'buttons.png'))
        self.button_sheet = pygame.transform.scale2x(buttons)
        self.quit_button = [592 * 2, 1 * 2, 64 * 2, 30 * 2]
        self.menu_button = [528 * 2, 1 * 2, 64 * 2, 30 * 2]
        self.restart_button = [304 * 2, 1 * 2, 80 * 2, 30 * 2]

    def draw_elements(self, scoreIn, highscore):
        """
        The method for displaying all elements onto the game over screen

        Displays the score, highscore, quit, menu, and restart buttons

        Parameters
        ----------
        scoreIn: int
            the current score achieved after the run
        highscore: int
            the highest score achieved of all time

        Returns
        -------
        quit_hitbox: pygame.Rect
            the rectangular hitbox for the quit button
        menu_hitbox: pygame.Rect
            the rectangular hitbox for the menu button
        restart_hitbox: pygame.Rect
            the rectangular hitbox for the restart button
        """

        hscore = self.score_font.render(f'High-score: {highscore}', True, (230, 230, 230), None)
        score = self.score_font.render(f'Score: {scoreIn}', True, (230, 230, 230), None)

        self.surface.blit(self.game_over, (270, 50))

        self.surface.blit(hscore, (100, 150))
        self.surface.blit(score, (100, 200))

        quit_hitbox = self.surface.blit(self.button_sheet, (600, 100), self.quit_button)
        menu_hitbox = self.surface.blit(self.button_sheet, (600, 170), self.menu_button)
        restart_hitbox = self.surface.blit(self.button_sheet, (569, 240), self.restart_button)

        return quit_hitbox, menu_hitbox, restart_hitbox
