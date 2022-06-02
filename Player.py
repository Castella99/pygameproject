import os
import Meeple


# 플레이어 객체
class Player:
    x_pos = 0  # 객체의 x좌표
    y_pos = 0  # 객체의 y좌표
    pos = (x_pos, y_pos)  # 객체의 좌표 튜플
    path = os.path.dirname(os.path.abspath(__file__))  # 경로 받아오기
    meeple = ["blue.png", "green.png", "purple.png", "red.png", "orange.png", "yellow.png"] # 말의 파일명 리스트
    num = 0 # meeple의 숫자
    board_num = 0 # 보드판 위의 meeple 숫자

    def __init__(self, num_of_meeple=1, mycolor=""):
        self.yut_result = []  # 던져서 나온 윷 결과를 저장함.
        self.color = mycolor
        self.state = 0  # 0=진행중, 1=1등, 2=2등, 3=3등, ...
        self.meeples = []
        self.num = num_of_meeple
        for i in range(self.num+1):
            if i == 0 :
                self.meeples.append(Meeple.Meeple(self.color, 0, 0, 0))
            else :
                self.meeples.append(Meeple.Meeple(self.color, 0, 0, 1))

    def move(self):
        pass
    