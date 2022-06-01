import pygame
import os


class Help:

    def __init__(self, main_surface, surfaceY):
        self.surface = main_surface
        self.surfaceY = surfaceY

        font = pygame.font.SysFont(name='impact', size=35)

        self.text = font.render('The Instructions Are Displayed in Your Browser.', True, (230, 230, 230), None)

        buttons = pygame.image.load(os.path.join('Game', 'Assets', 'Collidables', 'Game_States', 'buttons.png'))
        self.button_sheet = pygame.transform.scale(buttons, (656 * 4, 128 * 4))
        self.back_button = [56 * 4, 41 * 4, 13 * 4, 15 * 4]

    def draw_element(self):

        self.surface.blit(self.text, (37, 30))

        back_hitbox = self.surface.blit(self.button_sheet, (0, self.surfaceY - 55), self.back_button)

        return back_hitbox