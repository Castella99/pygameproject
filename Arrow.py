import os
import pygame


arrow_map = [
    (747, 648), (752, 540), (753, 427), (750, 315), (749, 205), (748, 97), (635, 92), (522, 95), (412, 94), (296, 96),
    (185, 95), (184, 204), (187, 318), (187, 428), (184, 539), (187, 655), (296, 656), (409, 655), (524, 653),
    (633, 653), (658, 183), (570, 266), (468, 368), (384, 453), (295, 538), (286, 197), (381, 284), (468, 368),
    (552, 460), (648, 555), (745, 650)
]


class Arrow:
    path = os.path.dirname(os.path.abspath(__file__))
    screen_width = 1080  # 스크린 가로
    screen_height = 720  # 스크린 세로
    arrow_images = [
        pygame.image.load(path + "/entity/up.png"),
        pygame.image.load(path + "/entity/down.png"),
        pygame.image.load(path + "/entity/left.png"),
        pygame.image.load(path + "/entity/right.png"),
        pygame.image.load(path + "/entity/rightup.png"),
        pygame.image.load(path + "/entity/leftup.png"),
        pygame.image.load(path + "/entity/rightdown.png"),
        pygame.image.load(path + "/entity/leftdown.png")
    ]
    arrow_dict = {
        "up": 0, "down": 1, "left": 2, "right": 3,
        "rightup": 4, "leftup": 5, "rightdown": 6, "leftdown": 7
    }

    def __init__(self, name, pos, state=False):
        self.image = self.arrow_images[self.arrow_dict[name]]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = pos[0] - (self.width / 2)
        self.y_pos = pos[1] - (self.height / 2)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos
        self.name = name
        # state False=해당 없음 / True=화면에 표시해야 함
        self.state = state
        # 몇번째 meeple의 화살표인지(idx)
        self.who = 0

    def set_state(self, state):
        self.state = state

    def set_arrow(self,state,who):
        self.state = state
        self.who = who