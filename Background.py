from Prototypegame import *
import os


class Background(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))

    background_images = [
        pygame.image.load(path + "/background/start.png"),
        pygame.image.load(path + "/background/table.png"),
        pygame.image.load(path + "/background/help.png"),
        pygame.image.load(path + "/background/finish.png")
    ]
    background_dict = {"start": 0, "table": 1, "help": 2, "finish": 3, }

    def __init__(self, prompt):
        super().__init__()
        self.background_image = self.background_images[self.background_dict[prompt]]

    def update_background(self, prompt):
        self.background_image = self.background_images[self.background_dict[prompt]]
