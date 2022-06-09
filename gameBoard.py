import os
import pygame.image


# 보드판 위치 (x, y)
# 크기: 80 * 80

"""
10 09 08 07 06 05
11 25       20 04
12  26     21  03
      22(27)
13  23     28  02
14 24       29 01
15 16 17 18 19 00(30)
"""
# 아래 board_map 은 위 00부터 20까지의 위치(칸)을 리스트로 넣어 놓은 것
board_map = [
    (602, 603), (607, 495), (608, 382), (605, 2270), (604, 160), (603, 52),
    (490, 47), (377, 50), (267, 49), (151, 51), (40, 50), (39, 159),
    (42, 273), (42, 383), (39, 494), (42, 610), (151, 611), (264, 610),
    (379, 608), (488, 608), (513, 138), (425, 221), (323, 323), (239, 408),
    (150, 493), (141, 152), (236, 239), (323, 323), (407, 415), (503, 510),
    (600, 605)
]
# 게임 스크린에 맞도록 보드칸 위치 값 수정
for x in range(len(board_map)):
    board_map[x] = list(board_map[x])
    board_map[x][0] += 138
    board_map[x][1] += 40
    board_map[x] = tuple(board_map[x])


# 게임보드판 객체 ()
class GameBoard:
    path = os.path.dirname(os.path.abspath(__file__))
    screen_width = 1080  # 스크린 가로
    screen_height = 720  # 스크린 세로

    # 선수 1이 00에 있으면 (4,4)=1, 선수 3이 15에 있으면 (3,2)=3, 선수 4가 16에 있으면 (2,2)=4
    """
    09 08 07 06 04
    11 10    05 03
    12    16    02
    13 15    17 01
    14 18 19 20 00
    """

    def __init__(self):
        self.image = pygame.image.load(self.path + "/entity/yutBoard.png")
        self.size = self.image.get_rect().size
        self.width = 650
        self.height = 650

        # 위치 나중에 수정할 것(뭔가 이상)
        self.x_pos = (3*self.screen_width/7) - (self.width/2)  # 138
        self.y_pos = (5*self.screen_height/9) - (self.screen_height/2)  # 40

        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

        # 게임 말이 위치에 있으면 1, 2, 3, 4로 업데이트 됨.
        self.board_state = [
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0,
        ]


if __name__ == "__main__":
    test = GameBoard()
    print(test.x_pos, test.y_pos)
    print(board_map)
