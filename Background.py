from Prototypegame import *
import os


class Background(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    prompt = "start"
    background_images = [
        pygame.image.load(path + "/background/empty.png"),
        pygame.image.load(path + "/background/start.png"),
        pygame.image.load(path + "/background/table color reverse.png"),
        pygame.image.load(path + "/background/help.PNG"),
        pygame.image.load(path + "/background/finish.png"),
        pygame.image.load(path + "/background/board.png")
    ]
    background_dict = {"empty": 0, "start": 1, "table": 2,
                       "help": 3, "finish": 4, "board": 5}

    def __init__(self, prompt):
        super().__init__()
        self.image = self.background_images[self.background_dict[prompt]]

    def put_image(self, prompt):
        self.image = self.background_images[self.background_dict[prompt]]
        return self.image
