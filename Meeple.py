import os
import pygame
from gameBoard import board_map

class Meeple:
    path = os.path.dirname(os.path.abspath(__file__))

    # 게임말 종류 6가지: 빨강, 주황, 노랑, 초록, 파랑, 보라 / 업기 3개까지
    mipple_images = {
        "red": [pygame.image.load(path + "/entity/mipple red1.png"),
                      pygame.image.load(path + "/entity/mipple red2.png"),
                      pygame.image.load(path + "/entity/mipple red3.png")],
        "orange": [pygame.image.load(path + "/entity/mipple orange1.png"),
                         pygame.image.load(path + "/entity/mipple orange2.png"),
                         pygame.image.load(path + "/entity/mipple orange3.png")]
        "yellow": [pygame.image.load(path + "/entity/mipple yellow1.png"),
                         pygame.image.load(path + "/entity/mipple yellow2.png"),
                         pygame.image.load(path + "/entity/mipple yellow3.png")],
        "green": [pygame.image.load(path + "/entity/mipple green1.png"),
                        pygame.image.load(path + "/entity/mipple green2.png"),
                        pygame.image.load(path + "/entity/mipple green3.png")],
        "blue": [pygame.image.load(path + "/entity/mipple blue1.png"),
                       pygame.image.load(path + "/entity/mipple blue2.png"),
                       pygame.image.load(path + "/entity/mipple blue3.png")],
        "purple": [pygame.image.load(path + "/entity/mipple purple1.png"),
                         pygame.image.load(path + "/entity/mipple purple2.png"),
                         pygame.image.load(path + "/entity/mipple purple3.png")]
    }
    def __init__(self, color="red" ,pos=0):
        self.color = color
        self.sum = 0
        self.pos = pos
        self.image = self.mipple_images[color][self.sum]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = board_map[pos][0]
        self.y_pos = board_map[pos][1]
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    # 게임 말 이동
    def move(self, pos):
        pos += 1
        self.x_pos = board_map[pos][0]
        self.y_pos = board_map[pos][1]

    # 다른 말 업기 (이미지 변경)
    def carry_my_back(self):
        self.sum += 1
        self.image = self.mipple_images[self.color][self.sum]



