from Prototypegame import*
import os


class Yut(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    yut_state = ["front", "front", "front", "front"]
    yut_dict = {"front": 0, "back": 1, "right": 2, "left": 3}
    result_dict = {"do": 1, "gae": 2, "geol": 3, "yut": 4, "mo": 5}
    yut_images = [
        pygame.image.load(path + "/entity/yut_front.png"),
        pygame.image.load(path + "/entity/yut_back.png"),
        pygame.image.load(path + "/entity/yut_right.png"),
        pygame.image.load(path + "/entity/yut_left.png")
    ]

    def __init__(self, prompt, pos1):
        self.image = self.yut_images[self.yut_dict[prompt]]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (pos1 * self.screen_width / 9) - (self.width / 2)
        self.y_pos = (self.screen_height / 2) - (self.height / 2)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    def position(self, pos):
        self.x_pos = (pos * self.screen_width / 9) - (self.width / 2)

    def result(self):
        rslt = 0
        for x in self.yut_state:
            rslt += x
        return x

    def put_image(self, prompt):
        self.image = self.yut_images[self.yut_dict[prompt]]
        return self.image
