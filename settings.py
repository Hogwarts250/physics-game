import pygame

class Settings():
    def __init__(self):
        self.screen_length = 1080
        self.screen_height = 720

        self.animation_speed = 0.15
        
        self.exit_flag = False
        self.world_flag = True

        self.padding = 20
        self.text_colour = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 30)

        self.player_move_speed = 0.7
        self.player_health = 10
        self.player_image = "images/player.png"
        self.image_locations = ["player_walk0.png", "player_walk1.png", "player_walk2.png", "player_walk3.png", "player_walk4.png", "player_walk5.png","player_walk6.png"]

        self.basic_enemy_move_speed = 0.3

        self.number_buttons = 3
        self.number_fight_enemies = 1

        self.level_tracker = 0
        self.enemy_counter = 0
    
    def reset(self):
        self.player_image = "images/player.png"
        self.player_health = 10
        self.enemy_counter = 0