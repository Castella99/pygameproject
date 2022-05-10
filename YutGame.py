from Prototypegame import*
import Yut
import gameBoard
import Meeple
import Button
import Background

import pygame.event
import os
import random


class YutGame(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))
    running = True
    push = False

    # 현재 게임 상태가 어떤지 확인 하는 변수
    title_screen = True
    setting_screen = False
    game_screen = False
    ending_screen = False

    # 현재 어떤 버튼이 눌렸나 확인하는 변수들
    home = True
    help = False
    board = False
    table = False
    green = False
    setting = False

    current_time = 0
    index = 0
    animation_time = None

    player = 1
    computer = 0

    def __init__(self):
        super().__init__()
        pygame.display.set_caption("yut Game")
        self.background = Background.Background("start")  # 배경 객체

        # 윷과 윷판 객체
        self.yut = Yut.Yut("front", 1)
        self.yut_board = gameBoard.GameBoard()

        self.animation_time = round(100 / len(self.yut.yut_images * 100), 2)

        # 게임말 한번 테스트 해봄 (수정해야 함.) ####################
        self.meeple1 = Meeple.Meeple("purple", 0)
        self.meeple2 = Meeple.Meeple("yellow", 0)
        self.meeple3 = Meeple.Meeple("blue", 0)
        #######################################################

        # 각종 버튼 객체
        self.start_button = Button.Button("start button", 1, 2, 2, 3)
        self.help_button = Button.Button("help button", 1, 2, 7, 8)
        self.home_button = Button.Button("home button", 8, 10, 1, 6)
        self.red_button = Button.Button("red button", 1, 2, 6, 7)
        self.green_button = Button.Button("green button", 1, 2, 6, 7)
        self.next_button = Button.Button("next button", 8, 9, 6, 7)
        self.restart_button = Button.Button("restart button", 1, 2, 2, 3)
        self.end_button = Button.Button("end button", 1, 2, 7, 8)
        self.down_button1 = Button.Button("down button", 7, 12, 3, 8)
        self.up_button1 = Button.Button("up button", 4, 5, 3, 8)
        self.down_button2 = Button.Button("down button", 7, 12, 5, 9)
        self.up_button2 = Button.Button("up button", 4, 5, 5, 9)

    def show_title_screen(self):  # 시작 화면 (규칙 설명으로 이동하고 다시 돌아 올 수 있음)
        # 간단한 이벤트 부분 (start, help home 버튼 클릭)
        for event in pygame.event.get():
            # 창 닫기 누르면 끝 부분(ENDING_SCREEN)으로 넘어감
            if event.type == pygame.QUIT:
                self.title_screen = False
                self.ending_screen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 시작버튼 누르면 중간부분(game_screen)의 보드판 화면으로 넘어감
                if self.start_button.rect.collidepoint(event.pos):
                    self.title_screen = False
                    self.setting_screen = True
                    self.setting = True
                # 도움버튼을 누르면 규칙 설명 화면으로 넘어감
                elif self.help_button.rect.collidepoint(event.pos):
                    self.help = True
                    self.home = False
                # 홈버튼을 누르면 시작화면으로 돌아감
                elif self.home_button.rect.collidepoint(event.pos):
                    self.home = True
                    self.help = False
        # 화면 출력 부분
        if self.home:  # 시작 화면과 시작 버튼, 도움 버튼
            self.screen.blit(self.background.put_image("start"), (0, 0))
            self.screen.blit(self.start_button.image,
                             (self.start_button.x_pos, self.start_button.y_pos))
            self.screen.blit(self.help_button.image,
                             (self.help_button.x_pos, self.help_button.y_pos))
        elif self.help:  # 규칙 설명 화면과 홈 버튼
            self.screen.blit(self.background.put_image("help"), (0, 0))
            self.screen.blit(self.home_button.image,
                             (self.home_button.x_pos, self.home_button.y_pos))
    
    def show_setting_screen(self):
        for event in pygame.event.get():
            # 창 닫기 누르면 끝 부분(ENDING_SCREEN)으로 넘어감
            if event.type == pygame.QUIT:
                self.setting_screen = False
                self.ending_screen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 시작버튼 누르면 중간부분(game_screen)의 보드판 화면으로 넘어감
                if self.down_button1.rect.collidepoint(event.pos):
                    if self.player == 1:
                        self.player = 1
                    else:
                        self.player -= 1
                elif self.up_button1.rect.collidepoint(event.pos):
                    if self.player + self.computer >= 6:
                        pass
                    else:
                        self.player += 1
                elif self.down_button2.rect.collidepoint(event.pos):
                    if self.computer == 0:
                        self.computer = 0
                    else:
                        self.computer -= 1
                elif self.up_button2.rect.collidepoint(event.pos):
                    if self.player + self.computer >= 7:
                        pass
                    else:
                        self.computer += 1
                elif self.next_button.rect.collidepoint(event.pos):
                    self.setting = False
                    self.setting_screen = False
                    self.game_screen = True
                    self.board = True
        self.player_text = self.game_font.render(str(self.player), True, (0, 0, 0))
        self.computer_text = self.game_font.render(str(self.computer), True, (0, 0, 0))

        if self.setting:
            self.screen.blit(self.background.put_image("setting"), (0, 0))
            self.button_screen_blit(self.next_button)
            self.button_screen_blit(self.down_button1)
            self.button_screen_blit(self.up_button1)
            self.button_screen_blit(self.down_button2)
            self.button_screen_blit(self.up_button2)
            self.screen.blit(self.player_text, (735, 260))
            self.screen.blit(self.computer_text, (735, 385))

    def show_game_screen(self):  # 게임 화면(윷놀이가 진행될 때의 화면)
        if self.board:
            self.yut.yut_state_reset()  # 윷을 모두 앞으로 리셋
            self.screen.blit(self.background.put_image("board"), (0, 0))
            self.screen.blit(self.next_button.image,
                             (self.next_button.x_pos, self.next_button.y_pos))
            self.screen.blit(self.yut_board.image,
                             (self.yut_board.x_pos, self.yut_board.y_pos))

            # 게임말 (수정할 것) ###########################################
            self.screen.blit(self.meeple1.image,
                             (self.meeple1.x_pos, self.meeple1.y_pos))
            self.screen.blit(self.meeple2.image,
                             (self.meeple2.x_pos, self.meeple2.y_pos))
            self.screen.blit(self.meeple3.image,
                             (self.meeple3.x_pos, self.meeple3.y_pos))
            ############################################################

        elif self.table:  # 윷 테이블로 이동하기 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("table"), (0, 0))
            self.screen.blit(self.green_button.image,
                             (self.green_button.x_pos, self.green_button.y_pos))
            self.screen.blit(self.next_button.image,
                             (self.next_button.x_pos, self.next_button.y_pos))
            self.yut.display_yut()
        if self.green:  # 윷 던지기(스페이스바)를 눌렀을 때
            if self.push:  # 스페이스바를 누르고 있을 때 윷 애니메이션 작동
                self.button()
                self.motion_update(60)
            else:  # 스페이스바를 뗐을 때 결과 출력
                self.yut.display_yut()
                self.screen.blit(self.red_button.image,
                                 (self.red_button.x_pos, self.red_button.y_pos))

    def main_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_screen = False
                self.ending_screen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # 클릭하면 말 이동하고 업기 해봄. #################################
                self.meeple1.move(1)  # 일단 한번 테스트 해봄 (무조건 바꿔야 함.)
                self.meeple2.move(2)
                self.meeple3.move(3)
                self.meeple1.carry_my_back()
                self.meeple2.carry_my_back()
                self.meeple3.carry_my_back()
                #############################################################

                if self.next_button.rect.collidepoint(event.pos) and self.board:
                    self.board = False
                    self.table = True
                elif self.next_button.rect.collidepoint(event.pos) and self.table:
                    self.board = True
                    self.table = False
                    self.green = False
                if self.green_button.rect.collidepoint(event.pos) and self.table:
                    self.green = True
                    self.push = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.push = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.table:
                    self.green = True
                    self.push = True
            elif event.type == pygame.KEYUP:
                self.push = False

    def check(self):  # 승패가 갈렸는지 확인 (미구현 상태)
        pass
        # if 승패가 나면:
        #   self.game_screen = False
        #   self.ending_screen = True

    def button(self):  # 윷 던지기(윷의 상태를 랜덤으로 생성 함)
        self.yut.yut_state.clear()  # 윷 상태 리스트 초기화
        for i in range(4):  # 윷 상태 만들기
            self.yut.yut_state.append(random.randrange(0, 1 + 1))  # 0, 1을 랜덤으로 받아서 추가
        print(self.yut.yut_state)

    def motion_update(self, mt):  # 윷이 돌아가는 애니메이션(수정 할 계획)
        self.current_time += mt
        print(self.current_time, self.animation_time)
        # 시간을 늦추는 역할?
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
            # 윷 사진의 인덱스를 넘어가면 0으로 초기화
            if self.index >= len(self.yut.yut_images):
                self.index = 0
            self.yut.image = self.yut.yut_images[self.index]  # 윷의 이미지는 앞, 우, 뒤, 좌로 돌아감
            self.yut.display_yut()  # 윷 4개 화면에 출력

    def show_ending_screen(self):  # 엔딩화면 (재시작과 종료버튼을 다룸)
        # 간단한 이벤트 부분 (restart, end 버튼 클릭 이벤트)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ending_screen = False  # 메인의 ending_screen while문을 빠져나감.
                self.running = False  # 메인의 running while문을 빠져나감.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 종료버튼을 누르면 게임이 종료됨.
                if self.end_button.rect.collidepoint(event.pos):
                    self.ending_screen = False
                    self.running = False
                # 다시시작 버튼을 누르면 시작부분(title_screen)의 시작화면으로 넘어감
                elif self.restart_button.rect.collidepoint(event.pos):
                    self.ending_screen = False; self.title_screen = True
                    self.home = True; self.help = False; self. board = False
                    self.table = False; self.green = False; self.push = False

        # 화면 출력 부분(끝배경, 종료버튼, 다시시작버튼)
        self.screen.blit(self.background.put_image("finish"), (0, 0))
        self.screen.blit(self.end_button.image,
                         (self.end_button.x_pos, self.end_button.y_pos))
        self.screen.blit(self.restart_button.image,
                         (self.restart_button.x_pos, self.restart_button.y_pos))

    def button_screen_blit(self, button):
        self.screen.blit(button.image, (button.x_pos, button.y_pos))


if __name__ == "__main__":
    pass
