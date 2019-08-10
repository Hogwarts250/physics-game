import sys, pygame
from pygame.sprite import Group

import game_functions

from player import Player
from button import Button
from settings import Settings

pygame.init()
settings = Settings()
screen_size = settings.screen_length, settings.screen_height
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Atom Land")

player = Player(screen, settings)
basic_enemies = Group()
button = Button("equation 1", screen)

game_functions.create_basic_enemies(screen, basic_enemies, settings)

while True:
    game_functions.check_pygame_events(player, button, settings)
    game_functions.update_sprites(player, basic_enemies, settings)

    game_functions.update_screen(player, basic_enemies, button, screen, settings)