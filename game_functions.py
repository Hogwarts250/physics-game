import pygame, sys

def check_pygame_events(player):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, player)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event, player)

def check_keydown_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = True

    elif event.key == pygame.K_LEFT:
        player.moving_left = True

    elif event.key == pygame.K_UP:
        player.moving_up = True

    elif event.key == pygame.K_DOWN:
        player.moving_down = True

def check_keyup_events(event, player):
    if event.key == pygame.K_RIGHT:
        player.moving_right = False

    elif event.key == pygame.K_LEFT:
        player.moving_left = False

    elif event.key == pygame.K_UP:
        player.moving_up = False

    elif event.key == pygame.K_DOWN:
        player.moving_down = False