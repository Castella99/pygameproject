from Prototypegame import*
import os


class Button(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    button_images = [
        pygame.image.load(path + "/entity/red button.png"),
        pygame.image.load(path + "/entity/green button.png"),
        pygame.image.load(path + "/entity/startButton.png"),
        pygame.image.load(path + "/entity/helpButton.png"),
        pygame.image.load(path + "/entity/next button.png")
    ]

    def __init__(self, image_num, pos1, pos2, pos3, pos4):
        super().__init__()
        self.button_image = self.button_images[image_num]
        self.button_size = self.button.get_rect().size
        self.button_width = self.button_size[0]
        self.button_height = self.button_size[1]
        self.button_x_pos = (pos1 * self.screen_width / pos2) - (self.button_width / 2)
        self.button_y_pos = (pos3 * self.screen_width / pos4) - (self.button_height / 2)
        self.button_rect = self.button.get_rect()
        self.button_rect.left = self.button_x_pos
        self.button_rect.top = self.button_y_pos


