class LevelDesign():
    def __init__(self, settings):
        self.areas = [0, 1, 2]
        self.settings = settings

        self.enemy_positions_area = {
            0 : [(32, settings.screen_height / 2), (settings.screen_length - 32, settings.screen_height / 2)], 
            1 : [(32, 32), (32, settings.screen_height - 32), (settings.screen_length - 32, 32), 
                    (settings.screen_length - 32, settings.screen_height - 32)]
        }
        
        self.question_options = {
            0 : ["1, 2, or 3?", "4, 5, or 6?"],
            1 : ["x, y, or z?", "j, k, or l?", "q, w, or e?", "r, s, or t?"]
        }

        self.text_options = {
            0 : [("1", "2", "3"), ("4", "5", "6")],
            1 : [("x", "y", "z"), ("j", "k", "l"), ("q", "w", "e"), ("r", "s", "t")]
        }

        self.hints = {
            0 : [("1", "2", "3"), ("4", "5", "6")],
            1 : [("x", "y", "z"), ("j", "k", "l"), ("q", "w", "e"), ("r", "s", "t")]
        }
