import pygame
from pygame.sprite import Sprite

class FightEnemy(Sprite):
    def __init__(self, hint, answer, screen, settings):
        super().__init__()

        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0, 0, 64, 64)

        self.hint = hint
        self.hint_trigger = False

        self.answer = answer

    def prep_text(self, text):
        self.text_image = self.settings.font.render(text, True, self.settings.text_colour)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.bottom = self.rect.top - 10
        self.text_rect.centerx = self.rect.centerx

    def draw_fight_enemy(self):
        pygame.draw.rect(self.screen, self.settings.text_colour, self.rect)
        if self.hint_trigger:
            self.prep_text(self.hint)
            self.screen.blit(self.text_image, self.text_rect)