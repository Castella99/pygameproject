import Meeple


# 플레이어 객체
class Player:
    def __init__(self, num_of_meeple=1, mycolor=""):
        self.yut_result = []  # 던져서 나온 윷 결과를 저장함.
        self.color = mycolor
        self.state = 0  # 0=진행중, 1=1등, 2=2등, 3=3등, ...
        self.meeples = []
        for i in range(num_of_meeple):
            self.meeples.append(Meeple.Meeple(self.color, 0, 0))

    def throw_yut(self):
        pass

    