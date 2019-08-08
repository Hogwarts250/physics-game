import pygame
from pygame.sprite import Sprite

from math import sin, cos, tan, atan

class BasicEnemy(Sprite):
    def __init__(self, screen):
        super().__init__

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(self.screen_rect.left, self.screen_rect.top, 100, 100)
        
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.move_speed = 0.3

    def update(self, player):
        self.centerx += sin(atan(player.centery - self.centery)) / tan(atan(player.centery - self.centery)) * self.move_speed
        self.centery += cos(atan(player.centery - self.centery)) * tan(atan(player.centery - self.centery)) * self.move_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    
    def draw_basic_enemy(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)