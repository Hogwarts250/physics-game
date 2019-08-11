import sys, pygame
from pygame.sprite import Group

import game_functions

from player import Player
from settings import Settings

from fight_enemy import FightEnemy

pygame.init()
settings = Settings()
screen_size = settings.screen_length, settings.screen_height
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Atom Land")

player = Player(screen, settings)

basic_enemies = Group()
game_functions.create_basic_enemies(screen, basic_enemies, settings)

buttons = []
game_functions.create_fight_gui(settings.number_buttons, buttons, screen, settings)

fight_enemy = FightEnemy("equation 1", screen)
fight_enemy.rect.centerx = 0.7 * settings.screen_length
fight_enemy.rect.centery = 0.5 * (0.75 * settings.screen_height - 20)

while True:
    game_functions.check_pygame_events(player, buttons, fight_enemy, settings)
    game_functions.update_sprites(player, basic_enemies, settings)

    game_functions.update_screen(player, basic_enemies, fight_enemy, buttons, screen, settings)