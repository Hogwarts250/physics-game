import pygame
from pygame.sprite import Sprite

class FightEnemy(Sprite):
    def __init__(self, answer, screen):
        super().__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, 64, 64)

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.answer = answer

    def draw_fight_enemy(self):
        pygame.draw.rect(self.screen, (255, 0, 0), self.rect)
