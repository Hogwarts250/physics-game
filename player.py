import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, screen):
        super().__init__

        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.rect = pygame.Rect(self.screen_rect.centerx, self.screen_rect.centery, 20, 20)

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.move_speed = 0.5

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.move_speed

        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.move_speed

        if self.moving_up and self.rect.top > 0:
            self.centery -= self.move_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.move_speed

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def draw_player(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
