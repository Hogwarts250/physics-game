import pygame
from pygame.sprite import Sprite

class BasicEnemy(Sprite):
    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.rect = pygame.Rect(self.screen_rect.left, self.screen_rect.top, 32, 32)
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.move_speed = self.settings.basic_enemy_move_speed

    def update(self, player):
        hypoteneuse = ((player.centery - self.centery) ** 2 + (player.centerx - self.centerx) ** 2) ** 0.5

        self.centerx += (player.centerx - self.centerx) * self.move_speed / hypoteneuse
        self.centery += (player.centery - self.centery) * self.move_speed / hypoteneuse

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def draw_basic_enemy(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect)