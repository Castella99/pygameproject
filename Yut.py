from Prototypegame import*
import os
import random

class YutGame(Prototype) :
    path = os.path.dirname(os.path.abspath(__file__))
    yut1 = None
    yut2 = None
    yut_size = None
    yut_width = None
    yut_height = None
    yut = [0, 0, 0, 0]
    button1 = None
    button2 = None
    button_size = None
    button_width = None
    button_height = None
    button_x_pos = None
    button_y_pos = None
    push = False
    running = True
    background = []
    start = True

    def __init__(self):
        super().__init__()
        pygame.display.set_caption(("yut Game"))
        self.background.append(pygame.image.load(self.path+"/background/start.png"))
        self.background.append(pygame.image.load(self.path+"/background/table.png"))
        self.yut1 = pygame.image.load(self.path+"/entity/yut1.png")
        self.yut2 = pygame.image.load(self.path+"/entity/yut3.png")
        self.yut_images = [
            pygame.image.load(self.path + "/entity/yut1.png"),
            pygame.image.load(self.path + "/entity/yut2.png"),
            pygame.image.load(self.path + "/entity/yut3.png"),
            pygame.image.load(self.path + "/entity/yut4.png")
        ]
        self.index = 0
        self.image = self.yut_images[self.index]
        self.animation_time = round(100 / len(self.yut_images * 100), 2)
        self.current_time = 0

        self.yut_size = self.yut1.get_rect().size
        self.yut_width = self.yut_size[0]
        self.yut_height = self.yut_size[1]
        self.button1 = pygame.image.load(self.path+"/entity/red button.png")
        self.button2 = pygame.image.load(self.path+"/entity/green button.png")
        self.button_size = self.button1.get_rect().size
        self.button_width = self.button_size[0]
        self.button_height = self.button_size[1]
        self.button_x_pos = (8 * self.screen_width / 9) - (self.button_width / 2)
        self.button_y_pos = (6 * self.screen_height / 7) - (self.button_height / 2)

    def redraw(self):
        self.screen.blit(self.background[1], (0, 0))  # 배경 그리기
        if self.push:
            self.screen.blit(self.button1, (self.button_x_pos, self.button_y_pos))
            self.motion_update(3000)
        else:
            self.screen.blit(self.button2, (self.button_x_pos, self.button_y_pos))
            for i in range(3, 6 + 1):
                if self.yut[i - 3] == 0:
                    self.screen.blit(self.yut1, ((i * self.screen_width / 9) - (self.yut_width / 2), (self.screen_height / 2) - (self.yut_height / 2)))
                else:
                    self.screen.blit(self.yut2, ((i * self.screen_width / 9) - (self.yut_width / 2), (self.screen_height / 2) - (self.yut_height / 2)))

    def button(self):
        self.push = True
        self.yut.clear()
        for i in range(4):
            self.yut.append(random.randrange(0, 1 + 1))
        print(self.yut)
        return self.push


    def motion_update(self, mt):
        self.current_time += mt
        print(self.current_time)
        if self.current_time >= 4000:
            self.current_time = 0
            self.index += 1
            if self.index >= len(self.yut_images):
                self.index = 0
            self.image = self.yut_images[self.index]
            for i in range(3, 6 + 1):
                self.screen.blit(self.image, ((i * self.screen_width / 9) - (self.yut_width / 2), (self.screen_height / 2) - (self.yut_height / 2)))


if __name__ == "__main__" :
    pass
