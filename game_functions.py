import pygame, sys

from basic_enemy import BasicEnemy
from settings import Settings

settings = Settings()

def check_pygame_events(player, button, settings):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if settings.world_flag:
                if event.type == pygame.KEYDOWN:
                    check_keydown_events(event, player)

                elif event.type == pygame.KEYUP:
                    check_keyup_events(event, player)
            
            elif settings.world_flag == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    check_button_clicked(button, mouse_x, mouse_y)

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

def check_button_clicked(button, mouse_x, mouse_y):
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    return button_clicked

def update_sprites(player, basic_enemies, settings):
    basic_enemies.update(player)
    player.update()

    if pygame.sprite.spritecollideany(player, basic_enemies):
        basic_enemies.remove(pygame.sprite.spritecollideany(player, basic_enemies))
        settings.world_flag = False

def update_screen(player, basic_enemies, button, screen, settings):
    screen.fill((255, 255, 255))

    if settings.world_flag:
        for enemy in basic_enemies:
            enemy.draw_basic_enemy()
        player.blitme()
    
    elif settings.world_flag == False:
        button.draw_button()

    pygame.display.flip()

def create_basic_enemies(screen, basic_enemies, settings):
    i = 0
    
    while i < settings.number_enemies:
        basic_enemy = BasicEnemy(screen, settings)
        basic_enemy.centerx += basic_enemy.centerx * i * (settings.screen_length / (14 * settings.number_enemies))
        basic_enemy.centery = basic_enemy.centery

        basic_enemy.rect.centerx = basic_enemy.centerx
        basic_enemy.rect.centery = basic_enemy.centery

        basic_enemies.add(basic_enemy)

        i += 1