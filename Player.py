import os
import Meeple


# 플레이어 객체
class Player:
    # 플레이어 순위
    score = 1
    x_pos = 0  # 객체의 x좌표
    y_pos = 0  # 객체의 y좌표
    pos = (x_pos, y_pos)  # 객체의 좌표 튜플
    path = os.path.dirname(os.path.abspath(__file__))  # 경로 받아오기

    num = 0  # meeple의 숫자
    board_num = 0  # 보드판 위 meeple의 개수
    mee_idx = 0  # 움직일 말의 숫자

    def __init__(self, num_of_meeple=1, mycolor="red"):
        self.yut_result = []  # 던져서 나온 윷 결과를 저장함.
        self.color = mycolor
        self.state = 0  # 0=진행중, 1=1등, 2=2등, 3=3등, ...
        self.meeples = []
        self.num = num_of_meeple  # meeple의 최대 개수
        self.idx = 0
        for i in range(self.num):
            self.meeples.append(Meeple.Meeple(self.color, 0, 0, 0))

    def set_mee_num(self, mee):
        self.mee_idx = mee

    # 몇개의 게임 말이 남았는지 확인; 보드에 게임 말을 몇개 더 올릴 수 있는지 확인
    def check_state(self):
        cnt = 0
        for meeple in self.meeples:
            if meeple.state != 0:
                cnt += 1
        if self.num == cnt:
            return True
        return  False

    # 남은 말의 개수가 없으면 True
    def check_done(self):
        for meeple in self.meeples:
            #print("게임말의 상태: ", meeple.state)
            if meeple.state != 2:
                return False
        print("True 리턴")
        return True

    # 잡히면 집으로 돌려보냄
    def go_home(self):
        pass