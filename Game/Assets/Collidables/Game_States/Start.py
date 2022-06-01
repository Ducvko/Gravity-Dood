import os
import pygame


class Title:

    def __init__(self, main_surface):
        self.surface = main_surface

        title_font = pygame.font.SysFont(name='impact', size=42)

        self.title = title_font.render('GRAVITY DOOD', True, (230, 230, 230), None)

        buttons = pygame.image.load(os.path.join('Game', 'Assets', 'Collidables', 'Game_States', 'buttons.png'))
        self.button_sheet = pygame.transform.scale2x(buttons)
        self.start_button = [384 * 2, 1 * 2, 64 * 2, 30 * 2]
        self.credits_button = [448 * 2, 1 * 2, 80 * 2, 30 * 2]

    def draw_elements(self):
        self.surface.blit(self.title, (255, 0))

        start_hitbox = self.surface.blit(self.button_sheet, (310, 130), self.start_button)

        credits_hitbox = self.surface.blit(self.button_sheet, (295, 190), self.credits_button)

        return start_hitbox, credits_hitbox


