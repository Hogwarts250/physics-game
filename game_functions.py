import pygame, sys
from random import randint

from basic_enemy import BasicEnemy
from fight_enemy import FightEnemy
from text_box import TextBox
from settings import Settings

def check_pygame_events(player, basic_enemies, fight_enemies, buttons, question_box, levels, screen, settings):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings.exit_flag = True
                sys.exit()

            if settings.world_flag:
                if event.type == pygame.KEYDOWN:
                    check_keydown_events(event, player)

                elif event.type == pygame.KEYUP:
                    check_keyup_events(event, player)
            
            elif settings.world_flag == False:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for button in buttons:
                        button_clicked(player, basic_enemies, button, buttons, fight_enemies, question_box, mouse_x, mouse_y, levels, screen, settings)

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

    elif event.key ==  pygame.K_DOWN:
        player.moving_down = False

def button_clicked(player, basic_enemies, button, buttons, fight_enemies, question_box, mouse_x, mouse_y, levels, screen, settings):
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    for fight_enemy in fight_enemies:
        # Changes from fight scene to world stage
        if button_clicked and button.text == fight_enemy.answer:
            fight_enemies.empty()
            question_box.clear()
            buttons.clear()
            settings.enemy_counter += 1

            if not basic_enemies:
                settings.level_tracker += 1
                settings.reset()
                player.rect.center = screen.get_rect().center
                player.centerx, player.centery = settings.screen_length / 2, settings.screen_height / 2
                
                create_basic_enemies(screen, basic_enemies, levels, settings)

            settings.world_flag = True
        
        elif button_clicked and button.text != fight_enemy.answer:
            fight_enemy.hint_trigger = True

def update_sprites(player, basic_enemies, fight_enemies, buttons, question_box, screen, levels, settings):
    if settings.world_flag:
        basic_enemies.update(player)
        player.update()

    elif settings.world_flag == False:
        pass

    if pygame.sprite.spritecollideany(player, basic_enemies):
        # Changes from world stage to fight scene
        basic_enemies.remove(pygame.sprite.spritecollideany(player, basic_enemies))
        player.reset()
        create_fight_gui(buttons, fight_enemies, question_box, screen, levels, settings)
        settings.world_flag = False

def update_screen(player, basic_enemies, fight_enemies, buttons, question_box, screen, settings):
    screen.fill((255, 255, 255))

    if settings.world_flag:
        for enemy in basic_enemies:
            enemy.draw_basic_enemy()

        player.blitme()
    
    elif settings.world_flag == False:
        for fight_enemy in fight_enemies:
            fight_enemy.draw_fight_enemy()

        for button in buttons:
            button.draw_text_box()

        for question in question_box:
            question.draw_text_box()

    pygame.display.flip()

def create_basic_enemies(screen, basic_enemies, levels, settings):
    starting_positions = levels.enemy_positions_area[settings.level_tracker]
    i = 0
    
    while i < len(starting_positions):
        position = starting_positions[i]

        basic_enemy = BasicEnemy(screen, settings)

        basic_enemy.centerx = position[0]
        basic_enemy.centery = position[1]
        basic_enemy.rect.centerx = basic_enemy.centerx
        basic_enemy.rect.centery = basic_enemy.centery

        basic_enemies.add(basic_enemy)

        i += 1

def create_fight_gui(buttons, fight_enemies, question_box, screen, levels, settings):
    question_options = levels.question_options[settings.level_tracker]
    question = question_options[settings.enemy_counter]

    level_text_options = levels.text_options[settings.level_tracker]
    text_options = level_text_options[settings.enemy_counter]

    level_hints = levels.hints[settings.level_tracker]
    hints = level_hints[settings.enemy_counter]

    i = 0

    while i < settings.number_buttons:
        create_button(buttons, text_options[i], (settings.screen_length - 80) / 3, settings.screen_height / 4, screen, settings)

        i += 1
    
    i = 0

    while i < settings.number_fight_enemies:
        random_int = randint(0, len(text_options) - 1)
        create_fight_enemy(fight_enemies, hints[random_int], text_options[random_int], screen, settings)
        
        i += 1

    question = TextBox(question, settings.screen_length - 2 * settings.padding, settings.screen_height / 12, screen, settings)
    question.rect.left = settings.padding
    question.rect.bottom = 3 * settings.screen_height / 4 - 2 * settings.padding
    question_box.append(question)

def create_button(buttons, text, width, height, screen, settings):
    button = TextBox(text, width, height, screen, settings)
    button.rect.left = button.width * len(buttons) + settings.padding * (len(buttons) + 1)
    button.rect.bottom = settings.screen_height - settings.padding
    buttons.append(button)

def create_fight_enemy(fight_enemies, hints, answer, screen, settings):
    fight_enemy = FightEnemy(hints, answer, screen, settings)
    fight_enemy.rect.centerx = 0.7 * settings.screen_length
    fight_enemy.rect.centery = 0.5 * (0.75 * settings.screen_height - settings.padding)

    fight_enemies.add(fight_enemy)