import Yut
from Prototypegame import*
import Button
import Background
import os
import random


class YutGame(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    running = True
    push = False

    start_background = True
    help_background = False
    table_background = False
    board_background = False
    finish_background = False

    start = False
    help = False
    home = True
    red = False
    green = False
    next = False
    restart = False

    background = Background.Background("start")
    start_button = Button.Button("start button", 1, 2, 2, 3)
    help_button = Button.Button("help button", 1, 2, 7, 8)
    home_button = Button.Button("home button", 9, 10, 1, 5)
    red_button = Button.Button("red button", 8, 9, 6, 7)
    green_button = Button.Button("green button", 8, 9, 6, 7)
    next_button = Button.Button("next button", 8, 9, 6, 7)
    restart_button = Button.Button("restart button", 1, 2, 2, 3)
    end_button = Button.Button("end button", 1, 2, 7, 8)
    yut = Yut.Yut("front", 1)

    def __init__(self):
        super().__init__()
        pygame.display.set_caption("yut Game")

    def show_Background_and_Button(self):
        if self.start:  # 시작 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("board"), (0, 0))
            self.screen.blit(self.next_button.image,
                             (self.next_button.x_pos, self.next_button.y_pos))
            self.start_background = False
            self.board_background = True
        elif self.help:  # 도움 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("help"), (0, 0))
            self.screen.blit(self.home_button.image,
                             (self.home_button.x_pos, self.home_button.y_pos))
            self.start_background = False
            self.help_background = True
        elif self.home:  # 홈 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("start"), (0, 0))
            self.screen.blit(self.start_button.image,
                             (self.start_button.x_pos, self.start_button.y_pos))
            self.screen.blit(self.help_button.image,
                             (self.help_button.x_pos, self.help_button.y_pos))
            self.help_background = False
            self.start_background = True
        elif self.green:  # 윷 던지기 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("table"), (0, 0))
            for i in range(3, 6 + 1):
                if not self.push:
                    self.yut.position(i)
                    self.screen.blit(self.yut.put_image(self.yut.yut_state[i-3]),
                                     (self.yut.x_pos, self.yut.y_pos))
                    self.screen.blit(self.red_button.image,
                                     (self.red_button.x_pos, self.red_button.y_pos))
                else:
                    self.yut.motion_update(20)
        elif self.red:  # 보드판으로 이동하기 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("board"), (0, 0))
            self.screen.blit(self.next_button.image,
                             (self.next_button.x_pos, self.next_button.y_pos))
            self.yut.yut_state = ["front", "front", "front", "front"]
            self.table_background = False
            self.board_background = True
        elif self.next:  # 윷 테이블로 이동하기 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("table"), (0, 0))
            self.screen.blit(self.green_button.image,
                             (self.green_button.x_pos, self.green_button.y_pos))
            for i in range(3, 6 + 1):
                self.yut.position(i)
                self.screen.blit(self.yut.put_image(self.yut.yut_state[i - 3]),
                                 (self.yut.x_pos, self.yut.y_pos))
            self.table_background = True
            self.board_background = False
        elif self.restart:  # 다시하기 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("help"), (0, 0))
            self.screen.blit(self.home_button.image,
                             (self.home_button.x_pos, self.home_button.y_pos))
            self.finish_background = False
            self.start_background = True

    def button(self):
        push = True
        self.yut.yut_state.clear()
        for i in range(4):
            if random.randrange(0, 1 + 1) == 0:
                self.yut.yut_state.append("front")
            else:
                self.yut.yut_state.append("back")
        return self.push


if __name__ == "__main__":
    pass
