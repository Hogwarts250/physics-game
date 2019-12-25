import threading
import time

class Animate(threading.Thread):
    """ A class that creates a seperate thread to animate a sprite """

    def __init__(self, base_path, settings):
        super().__init__()

        self.settings = settings
        self.base_path = base_path

        self.image_counter = 0
    
    def run(self):
        while True:
            if self.settings.game_over_flag:
                break
            
            self.settings.player_image = self.base_path + str(self.image_counter) + ".png"
            time.sleep(self.settings.animation_speed)
            self.image_counter += 1
            
            if self.image_counter == len(self.settings. image_locations):
                self.image_counter = 0
 