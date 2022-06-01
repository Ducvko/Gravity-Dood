import pygame
import os


class GameOver:

    def __init__(self, main_surface):
        self.surface = main_surface

        font = pygame.font.SysFont(name='impact', size=50)

        self.game_over = font.render('GAME OVER!', True, (230, 230, 230), None)

        self.score_font = pygame.font.SysFont(name='trebuchetms', size=35)

        buttons = pygame.image.load(os.path.join('Game', 'Assets', 'Collidables', 'Game_States', 'buttons.png'))
        self.button_sheet = pygame.transform.scale2x(buttons)
        self.quit_button = [592 * 2, 1 * 2, 64 * 2, 30 * 2]
        self.menu_button = [528 * 2, 1 * 2, 64 * 2, 30 * 2]
        self.restart_button = [304 * 2, 1 * 2, 80 * 2, 30 * 2]

    def draw_elements(self, scoreIn, highscore):
        hscore = self.score_font.render(f'High-score: {highscore}', True, (230, 230, 230), None)
        score = self.score_font.render(f'Score: {scoreIn}', True, (230, 230, 230), None)

        self.surface.blit(self.game_over, (270, 50))

        self.surface.blit(hscore, (100, 150))
        self.surface.blit(score, (100, 200))

        quit_hitbox = self.surface.blit(self.button_sheet, (600, 100), self.quit_button)
        menu_hitbox = self.surface.blit(self.button_sheet, (600, 170), self.menu_button)
        restart_hitbox = self.surface.blit(self.button_sheet, (569, 240), self.restart_button)

        return quit_hitbox, menu_hitbox, restart_hitbox
