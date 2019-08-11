import pygame.font
import pygame

class Button():
    def __init__(self, text, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = (self.screen_rect.width - 80) / 3
        self.height = self.screen_rect.height / 4

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.border_colour = (0, 0, 0)
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)
        self.text = text

    def prep_text(self, text):
        self.text_image = self.font.render(text, True, self.text_colour)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center

    def draw_button(self):
        pygame.draw.rect(self.screen, self.border_colour, self.rect, 3)
        self.prep_text(self.text)
        self.screen.blit(self.text_image, self.text_rect)