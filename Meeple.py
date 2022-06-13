import os
import pygame

import gameBoard
from gameBoard import board_map


# 게임 말 객체 (다음 칸으로 이동하기, 업기 메소드 포함)
class Meeple:
    path = os.path.dirname(os.path.abspath(__file__))
    sound_idx = 0
    # 게임말 종류 6가지: 빨강, 주황, 노랑, 초록, 파랑, 보라
    # 기본은 1이고 업을 때마다 2, 3으로 갱신 (업기 2개까지)
    mipple_images = {
        "red": [pygame.image.load(path + "/meeple/mipple red1.png"),
                pygame.image.load(path + "/meeple/mipple red2.png"),
                pygame.image.load(path + "/meeple/mipple red3.png")],
        "orange": [pygame.image.load(path + "/meeple/mipple orange1.png"),
                   pygame.image.load(path + "/meeple/mipple orange2.png"),
                   pygame.image.load(path + "/meeple/mipple orange3.png")],
        "yellow": [pygame.image.load(path + "/meeple/mipple yellow1.png"),
                   pygame.image.load(path + "/meeple/mipple yellow2.png"),
                   pygame.image.load(path + "/meeple/mipple yellow3.png")],
        "green": [pygame.image.load(path + "/meeple/mipple green1.png"),
                  pygame.image.load(path + "/meeple/mipple green2.png"),
                  pygame.image.load(path + "/meeple/mipple green3.png")],
        "blue": [pygame.image.load(path + "/meeple/mipple blue1.png"),
                 pygame.image.load(path + "/meeple/mipple blue2.png"),
                 pygame.image.load(path + "/meeple/mipple blue3.png")],
        "purple": [pygame.image.load(path + "/meeple/mipple purple1.png"),
                   pygame.image.load(path + "/meeple/mipple purple2.png"),
                   pygame.image.load(path + "/meeple/mipple purple3.png")],
        "void": [pygame.image.load(path + "/meeple/void.png"),
                 pygame.image.load(path + "/meeple/void2.png")]
    }

    def __init__(self, color="red", pos=0, state=0, sum=0):
        self.color = color  # 내 게임 말의 색깔
        self.sum = sum  # (업은 수)
        self.pos = pos  # 내가 현재 위치하는 칸
        self.state = state  # 0=아직, 1=보드위, 2=통과, 3=업힘
        self.who_back = -1 # 몇번째 idx meeple에게 업혀있는지
        # -1: 업혀있지 않음, 0: 0번째 말에게 업힘, 1: 1번째 말에게 업힘, 2: 2번째 말에게 업힘.

        # 효과음들
        self.move_sound = [
            pygame.mixer.Sound(self.path + "/sound/a.wav"),
            pygame.mixer.Sound(self.path + "/sound/b.wav"),
            pygame.mixer.Sound(self.path + "/sound/c.wav"),
            pygame.mixer.Sound(self.path + "/sound/d.wav"),
            pygame.mixer.Sound(self.path + "/sound/e.wav")
        ]


        self.image = self.mipple_images[color][self.sum]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = board_map[self.pos][0] - (self.width / 2)
        self.y_pos = board_map[self.pos][1] - (self.height / 2)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos - 30
        self.rect.top = self.y_pos - 30

    # 게임 말 이동 (num 만큼 칸을 이동함) (수정 필요)
    # ex) 도이면 num=1, 윷이면 num=4
    def move(self, arrow):
        # 게임 말이 보드판을 완주하면
        if self.state == 2 or self.pos == 31:
            self.state = 2
            self.pos = 31
            return
        #self.move_sound[Meeple.sound_idx].play()
        Meeple.sound_idx += 1
        if arrow == 0:
            self.pos += 1
        elif arrow == 1:
            self.pos += 1
        elif arrow == 2:
            if self.pos == 5:
                self.pos += 15
            elif self.pos == 24:
                self.pos -= 9
            else:
                self.pos += 1
        elif arrow == 3:
            self.pos += 1
        elif arrow == 4:
            if self.pos == 10:
                self.pos += 15
            else:
                self.pos += 1
        elif arrow == 5:
            if self.pos == 19:
                self.pos += 11
            else:
                self.pos += 1
        elif arrow == 6:
            if self.pos == 15:
                self.pos += 9
            elif self.pos == 24:
                self.pos -= 1
            elif self.pos == 23:
                self.pos += 4
            else:
                self.pos += 1
        elif arrow == 7:
            if self.pos == 22:
                self.pos += 4
            elif self.pos == 26:
                self.pos -= 1
            elif self.pos == 25:
                self.pos -= 15
            else:
                self.pos += 1
        elif arrow == 8:
            if self.pos == 22:
                self.pos += 6
            else:
                self.pos += 1
        elif arrow == 9:
            if self.pos == 24:
                self.pos -= 9
            else:
                self.pos += 1
        elif arrow == -1:
            if self.pos == 24:
                self.pos -= 9
            elif self.pos == 19:
                self.pos += 11
            else:
                self.pos += 1

        self.x_pos = board_map[self.pos][0] - (self.width / 2)
        self.y_pos = board_map[self.pos][1] - (self.height / 2)
        self.state = 1


    # sum에 맞게 이미지를 변경한다.
    # 기본은 0, 하나 업으면 1, 두개 업으면 2
    def change_sum_and_image(self, sum):
        self.sum = sum
        self.image = self.mipple_images[self.color][self.sum]

    # 게임말 선택 화면에서 사용함.
    def set_rect(self):
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    # process4 말 선택할때 사용
    def set_left_top(self):
        self.rect.left = self.x_pos - 30
        self.rect.top = self.y_pos - 30

    def set_void(self):
        self.image = self.mipple_images["void"][0]

    def minus_sum(self):
        self.sum -= 1
        self.image = self.mipple_images[self.color][self.sum]

    # 보드 옆 상태창에 게임말 표시할 때 사용
    def set_pos(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.set_rect()