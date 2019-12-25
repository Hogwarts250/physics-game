import pygame
from pygame.sprite import Sprite
from random import randint

class BasicEnemy(Sprite):
    """ A class that represents a single, simple enemy in the world """

    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0, 0, 64, 64)
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.move_speed = self.settings.basic_enemy_move_speed + randint(0, 20) / 100

    def update(self, player):
        hypoteneuse = ((player.centery - self.centery) ** 2 + (player.centerx - self.centerx) ** 2) ** 0.5

        self.centerx += (player.centerx - self.centerx) * self.move_speed / hypoteneuse
        self.centery += (player.centery - self.centery) * self.move_speed / hypoteneuse

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def draw_basic_enemy(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)