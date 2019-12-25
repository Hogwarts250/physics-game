class LevelDesign():
    """ A class that stores all the levels for the game """

    def __init__(self, settings):
        self.areas = [0, 1, 2]
        self.settings = settings

        self.enemy_positions_area = {
            0 : [(settings.screen_length / 2, 32), (settings.screen_length / 2, settings.screen_height / 3)], 
            1 : [(32, 32), (32, settings.screen_height - 32), (settings.screen_length - 32, 32), 
                    (settings.screen_length - 32, settings.screen_height - 32)],
            2 : [(settings.screen_length / 2, settings.screen_height / 4)]
        }
        
        self.question_options = {
            0 : ["What does the 'd' in the equation d = v t stand for?", "4, 5, or 6?"],
            1 : ["x, y, or z?", "a, b, or c?", "q, w, or e?", "r, s, or t?"],
            2 : ["asdf, qwer, jkl;"]
        }

        self.text_options = {
            0 : [("direction", "distance", "displacement"), ("4", "5", "6")],
            1 : [("x", "y", "z"), ("a", "b", "c"), ("q", "w", "e"), ("r", "s", "t")],
            2 : [("asdf", "qwer", "jkl;")]
        }
        
        self.answers = {
            0 : ["distance", "4"],
            1 : ["z", "a", "w", "t"],
            2 : ["jkl;"]
        }

        self.hints = {
            0 : ["scalar meseurement", "4"],
            1 : ["z", "a", "w", "t"],
            2 : ["jkl;"]
        }
