import pygame

class TextBox():
    def __init__(self, text, width, height, screen, settings):
        self.screen = screen
        self.settings = settings

        self.width = width
        self.height = height

        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.text = text

    def prep_text(self, text):
        self.text_image = self.settings.font.render(text, True, self.settings.text_colour)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center

    def draw_text_box(self):
        pygame.draw.rect(self.screen, self.settings.text_colour, self.rect, 3)
        self.prep_text(self.text)
        self.screen.blit(self.text_image, self.text_rect)