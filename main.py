import sys, pygame

from player import Player
from basic_enemy import BasicEnemy

import game_functions

pygame.init()
screen_size = 1080, 720
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Atom Land")

player = Player(screen)
basic_enemy = BasicEnemy(screen)

while True:
    game_functions.check_pygame_events(player)

    screen.fill((0, 0, 0))

    player.update()
    basic_enemy.update(player)

    basic_enemy.draw_basic_enemy()
    player.draw_player()
        
    pygame.display.flip()