from Prototypegame import*
import os


class Button(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    button_images = [
        pygame.image.load(path + "/entity/red button.png"),
        pygame.image.load(path + "/entity/green button.png"),
        pygame.image.load(path + "/entity/startButton.png"),
        pygame.image.load(path + "/entity/helpButton.png"),
        pygame.image.load(path + "/entity/home.png"),
        pygame.image.load(path + "/entity/next button.png"),
        pygame.image.load(path + "/entity/end button.png"),
        pygame.image.load(path + "/entity/restart button.png")
    ]
    show_button = None
    button_dict = {"red button": 0, "green button": 1, "start button": 2,
                   "help button": 3, "home button": 4, "next button": 5,
                   "end button": 6, "restart button": 7}

    def __init__(self, prompt, pos1, pos2, pos3, pos4):
        super().__init__()
        self.image = self.button_images[self.button_dict[prompt]]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (pos1 * self.screen_width / pos2) - (self.width / 2)
        self.y_pos = (pos3 * self.screen_height / pos4) - (self.height / 2)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos


