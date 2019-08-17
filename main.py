import sys, pygame
from pygame.sprite import Group
from _thread import start_new_thread

import game_functions

from player import Player
from text_box import TextBox
from level_design import LevelDesign
from settings import Settings

from animate import Animate

pygame.init()

settings = Settings()
screen_size = settings.screen_length, settings.screen_height
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Atom Land")

levels = LevelDesign(settings)
player = Player(screen, settings)

basic_enemies = Group()
game_functions.create_basic_enemies(screen, basic_enemies, levels, settings)

buttons = []
fight_enemies = Group()
question_box = []

animate = Animate(settings)

animate.start()
 
while True:
    game_functions.check_pygame_events(player, basic_enemies, fight_enemies, buttons, question_box, levels, screen, settings)
    game_functions.update_sprites(player, basic_enemies, fight_enemies, buttons, question_box, screen, levels, settings)

    game_functions.update_screen(player, basic_enemies, fight_enemies, buttons, question_box, screen, settings)
