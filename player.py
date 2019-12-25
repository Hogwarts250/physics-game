import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    """ A class that represents the user """

    def __init__(self, screen, settings):
        super().__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        
        self.image = pygame.image.load(self.settings.player_image)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.move_speed = self.settings.player_move_speed

        self.health = self.settings.player_health

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

        self.image = pygame.image.load(self.settings.player_image)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def reset(self):
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False