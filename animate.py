import threading
import time

class Animate(threading.Thread):
    def __init__(self, settings):
        super().__init__()

        self.settings = settings

        self.image_counter = 0
    
    def run(self):
        while True:
            if self.settings.exit_flag:
                break
            
            self.settings.player_image = "images/player_walk_down/" + "player_walk" + str(self.image_counter) + ".png"
            time.sleep(self.settings.animation_speed)
            self.image_counter += 1
            
            if self.image_counter == len(self.settings. image_locations):
                self.image_counter = 0
 