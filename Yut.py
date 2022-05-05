from Prototypegame import*
import os


class Yut(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    yut_state = [0, 0, 0, 0]  # 윷의 결과(상태) 모두 앞면을 바라보도록 초기화
    yut_dict = {"front": 0, "back": 1, "right": 2, "left": 3}  # 윷의 모양을 딕셔너리로 만듦. (prompt로 사용)
    result_dict = {"do": 1, "gae": 2, "geol": 3, "yut": 4, "mo": 5}  # 도, 개, 걸, 윷, 모
    yut_images = [
        pygame.image.load(path + "/entity/yut_front.png"),
        pygame.image.load(path + "/entity/yut_back.png"),
        pygame.image.load(path + "/entity/yut_right.png"),
        pygame.image.load(path + "/entity/yut_left.png")
    ]

    def __init__(self, prompt, pos1):
        super().__init__()
        self.image = self.yut_images[self.yut_dict[prompt]]
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x_pos = (pos1 * self.screen_width / 9) - (self.width / 2)
        self.y_pos = (self.screen_height / 2) - (self.height / 2)
        self.rect = self.image.get_rect()
        self.rect.left = self.x_pos
        self.rect.top = self.y_pos

    def position(self, pos):  # 윷의 위치를 정해주는 함수
        self.x_pos = (pos * self.screen_width / 9) - (self.width / 2)

    def result(self):  # 아직 사용 안함 나중을 위해 만듦 (바꿀 수도 있음)
        rslt = 0
        for x in self.yut_state:
            rslt += x
        print("윷의 결과는 ", x)
        return x

    def put_image(self, prompt):  # 윷 객체의 사진을 prompt에 맞는 사진으로 바꿈(앞, 뒤, 오른쪽, 왼쪽)
        self.image = self.yut_images[self.yut_dict[prompt]]
        return self.image

    def put_image(self, num):  # 메소드 오버로딩 (윷 사진을 정수로 입력 받는 형태)
        self.image = self.yut_images[num]
        return self.image

    def display_yut(self):  # 윷 4개를 화면에 보임
        for i in range(3, 6 + 1):
            self.position(i)
            self.screen.blit(self.put_image(self.yut_state[i - 3]),
                             (self.x_pos, self.y_pos))

    def yut_state_reset(self):  # 윷 상태를 모두 앞으로 초기화 함.
        self.yut_state = [0, 0, 0, 0]

