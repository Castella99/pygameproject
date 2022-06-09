import os
import pygame

import gameBoard
from gameBoard import board_map

# 게임 말 객체 (다음 칸으로 이동하기, 업기 메소드 포함)
class Meeple:
    path = os.path.dirname(os.path.abspath(__file__))

    # 게임말 종류 6가지: 빨강, 주황, 노랑, 초록, 파랑, 보라
    # 기본은 1이고 업을 때마다 2, 3으로 갱신 (업기 2개까지)
    mipple_images = {
        "red": [pygame.image.load(path+ "/meeple/red.png"),
                pygame.image.load(path + "/meeple/mipple red1.png"),
                pygame.image.load(path + "/meeple/mipple red2.png"),
                pygame.image.load(path + "/meeple/mipple red3.png")],
        "orange": [pygame.image.load(path+ "/meeple/orange.png"),
                    pygame.image.load(path + "/meeple/mipple orange1.png"),
                   pygame.image.load(path + "/meeple/mipple orange2.png"),
                   pygame.image.load(path + "/meeple/mipple orange3.png")],
        "yellow": [pygame.image.load(path+ "/meeple/yellow.png"),
                   pygame.image.load(path + "/meeple/mipple yellow1.png"),
                   pygame.image.load(path + "/meeple/mipple yellow2.png"),
                   pygame.image.load(path + "/meeple/mipple yellow3.png")],
        "green": [pygame.image.load(path+ "/meeple/green.png"),
                  pygame.image.load(path + "/meeple/mipple green1.png"),
                  pygame.image.load(path + "/meeple/mipple green2.png"),
                  pygame.image.load(path + "/meeple/mipple green3.png")],
        "blue": [pygame.image.load(path+ "/meeple/blue.png"),
                 pygame.image.load(path + "/meeple/mipple blue1.png"),
                 pygame.image.load(path + "/meeple/mipple blue2.png"),
                 pygame.image.load(path + "/meeple/mipple blue3.png")],
        "purple": [pygame.image.load(path+ "/meeple/purple.png"),
                   pygame.image.load(path + "/meeple/mipple purple1.png"),
                   pygame.image.load(path + "/meeple/mipple purple2.png"),
                   pygame.image.load(path + "/meeple/mipple purple3.png")],
        "void": [pygame.image.load(path + "/meeple/void.png")]
    }

    def __init__(self, color="red", pos=0, state=0, sum=1):
        self.color = color  # 내 게임 말의 색깔
        self.sum = sum  # 업은 수
        self.pos = pos  # 내가 현재 위치하는 칸
        self.state = state  # 0=아직, 1=보드위, 2=통과
        self.image = self.mipple_images[color][self.sum]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = board_map[self.pos][0] - (self.width / 2)
        self.y_pos = board_map[self.pos][1] - (self.height / 2)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    # 게임 말 이동 (num 만큼 칸을 이동함) (수정 필요)
    # ex) 도이면 num=1, 윷이면 num=4
    def move(self, num):
        self.pos += num
        if self.pos >= len(gameBoard.board_map):
            self.pos = 0
        self.x_pos = board_map[self.pos][0] - (self.width/2)
        self.y_pos = board_map[self.pos][1] - (self.height/2)

    # 다른 말 업기 (이미지 변경)
    # 기본은 1, 하나 업으면 2, 두개 업으면 3
    def carry_my_back(self):
        self.sum += 1
        if self.sum == 4:
            self.sum = 1
        self.image = self.mipple_images[self.color][self.sum]

    def set_rect(self):
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    def set_void(self):
        self.image = self.mipple_images["void"][0]

    def minus_sum(self):
        self.sum -= 1
        self.image = self.mipple_images[self.color][self.sum]

    def set_pos(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.set_rect()