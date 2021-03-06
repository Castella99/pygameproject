import os
import pygame.image


# 보드판 위치 (x, y)
# 크기: 80 * 80
x = -999
board_pos = [
    [(48, 48), (185, 50), (315, 55), (470, 50), (600, 50)],
    [(50, 188), (190, 200), (x, x), (440, 217), (600, 175)],
    [(45, 325), (x, x), (310, 330), (x, x), (590, 325)],
    [(43, 470), (190, 455), (x, x), (440, 450), (595, 455)],
    [(48, 595), (185, 595), (315, 595), (470, 595), (600, 595)],
]
"""
09 08 07 06 04
11 10    05 03
12    16    02
13 15    17 01
14 18 19 20 00
"""
# 아래 board_map 은 위 00부터 20까지의 위치(칸)을 리스트로 넣어 놓은 것
board_map = [board_pos[4][4], board_pos[3][4], board_pos[2][4], board_pos[1][4],
             board_pos[0][4], board_pos[1][3], board_pos[0][3], board_pos[0][2],
             board_pos[0][1], board_pos[0][0], board_pos[1][1], board_pos[1][0],
             board_pos[2][0], board_pos[3][0], board_pos[4][0], board_pos[3][1],
             board_pos[2][2], board_pos[3][3], board_pos[4][1], board_pos[4][2],
             board_pos[4][3]]
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

    # 게임 말이 위치에 있으면 1, 2, 3, 4로 업데이트 됨. (어쩌면 사옹 안 할 수도?)
    board_state = [
        [0, 0, 0, 0, 0],
        [0, 0, x, 0, 0],
        [0, x, 0, x, 0],
        [0, 0, x, 0, 0],
        [0, 0, 0, 0, 0]
    ]
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


if __name__ == "__main__":
    test = GameBoard()
    print(test.x_pos, test.y_pos)
    print(board_map)
