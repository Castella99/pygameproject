import time

from Prototypegame import*
import Yut
import gameBoard
import Meeple
import Button
import Background
import Player
import Computer

import pygame
import os
import random


class YutGame(Prototype):
    def __init__(self):
        super().__init__()
        print("게임이 생성 되었습니다.")

        self.path = os.path.dirname(os.path.abspath(__file__))
        self.running = True
        self.push = False

        # 현재 게임 상태가 어떤지 확인 하는 변수
        self.screen_title = True
        self.screen_setting = False
        self.screen_meeple = False
        self.screen_game = False
        self.screen_ending = False


        # 현재 어떤 버튼이 눌렸나 확인하는 변수들
        self.button_home = True
        self.button_help = False
        self.button_board = False
        self.button_table = False
        self.button_green = False
        self.button_setting = False
        self.button_meeple = False

        self.current_time = 0
        self.index = 0
        self.animation_time = None
        #  초기 설정: 사람의 수와 컴퓨터의 수와 인당 가질 말의 수를 결정하는 변수 (컴퓨터수와 사람의 수의 합은 6)
        self.num_of_player = 1
        self.num_of_computer = 0
        self.num_of_meeple = 1

        self.meeple_button_list = []
        self.meeple_color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.init_text = 0
        self.next_board = False

        self.player_list = []
        self.computer_list = []
        self.computer_mee_list = [1, 2, 3, 4, 5, 6]
        self.setcomputer = True
        self.order = []  # 플레이어 총 순서
        self.meeple_move = False  # 윷을 던지고 말을 움직이게 하는 변수
        self.order_idx = 0  # 현재 순번의 말
        self.yut_rst = 0  # 윳 던진 결과
        self.screen_mee_list = []  # 스크린상에 표시되어야할 말
        self.mee_button = []

        pygame.display.set_caption("yut Game")
        self.background = Background.Background("start")  # 배경 객체

        # 윷과 윷판 객체
        self.yut = Yut.Yut("front", 1)
        self.yut_board = gameBoard.GameBoard()

        self.animation_time = round(100 / len(self.yut.yut_images * 100), 2)


        # 각종 버튼 객체
        self.start_button = Button.Button("start button", 1, 2, 2, 3)
        self.help_button = Button.Button("help button", 1, 2, 7, 8)
        self.home_button = Button.Button("home button", 8, 10, 1, 6)
        self.red_button = Button.Button("red button", 1, 2, 7, 9)
        self.green_button = Button.Button("green button", 1, 2, 7, 9)
        self.next_button = Button.Button("next button", 8, 9, 6, 7)
        self.next_button_up = Button.Button("next button", 8, 9, 1, 7)
        self.restart_button = Button.Button("restart button", 1, 2, 2, 3)
        self.end_button = Button.Button("end button", 1, 2, 7, 8)
        self.down_button1 = Button.Button("down button", 7, 12, 3, 8)
        self.up_button1 = Button.Button("up button", 4, 5, 3, 8)
        self.down_button2 = Button.Button("down button", 7, 12, 5, 9)
        self.up_button2 = Button.Button("up button", 4, 5, 5, 9)
        self.down_button3 = Button.Button("down button", 7, 12, 7, 9)
        self.up_button3 = Button.Button("up button", 4, 5, 7, 9)

        for color in self.meeple_color_list:
            self.meeple_button_list.append(Meeple.Meeple(color, 0, 0, 0))

    def __del__(self):
        print("게임이 제거 되었습니다.")

    # 시작 화면 (규칙 설명으로 이동하고 다시 돌아 올 수 있음)
    def show_title_screen(self):
        # 간단한 이벤트 부분 (start, help home 버튼 클릭)
        for event in pygame.event.get():
            # 창 닫기 누르면 끝 부분(ENDING_SCREEN)으로 넘어감
            if event.type == pygame.QUIT:
                self.screen_title = False
                self.screen_ending = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 시작버튼 누르면 중간부분(game_screen)의 보드판 화면으로 넘어감
                if self.start_button.rect.collidepoint(event.pos):
                    self.screen_title = False
                    self.screen_setting = True
                    self.button_setting = True
                # 도움버튼을 누르면 규칙 설명 화면으로 넘어감
                elif self.help_button.rect.collidepoint(event.pos):
                    self.button_help = True
                    self.button_home = False
                # 홈버튼을 누르면 시작화면으로 돌아감
                elif self.home_button.rect.collidepoint(event.pos):
                    self.button_home = True
                    self.button_help = False

        # 화면 출력 부분
        if self.button_home:  # 시작 화면과 시작 버튼, 도움 버튼
            self.screen.blit(self.background.put_image("start"), (0, 0))
            self.screen.blit(self.start_button.image,
                             (self.start_button.x_pos, self.start_button.y_pos))
            self.screen.blit(self.help_button.image,
                             (self.help_button.x_pos, self.help_button.y_pos))
        elif self.button_help:  # 규칙 설명 화면과 홈 버튼
            self.screen.blit(self.background.put_image("help"), (0, 0))
            self.screen.blit(self.home_button.image,
                             (self.home_button.x_pos, self.home_button.y_pos))

    # 플레이어 수, 게임말 개수 설정 화면
    def show_setting_screen(self):
        # 이벤트 처리
        for event in pygame.event.get():
            # 창 닫기 누르면 끝 부분(ENDING_SCREEN)으로 넘어감
            if event.type == pygame.QUIT:
                self.screen_setting = False
                self.screen_ending = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 시작버튼 누르면 중간부분(game_screen)의 보드판 화면으로 넘어감
                if self.down_button1.rect.collidepoint(event.pos):
                    if self.num_of_player == 1:
                        self.num_of_player = 1
                    else:
                        self.num_of_player -= 1
                elif self.up_button1.rect.collidepoint(event.pos):
                    if self.num_of_player + self.num_of_computer >= 6:
                        pass
                    else:
                        self.num_of_player += 1
                elif self.down_button2.rect.collidepoint(event.pos):
                    if self.num_of_computer == 0:
                        self.num_of_computer = 0
                    else:
                        self.num_of_computer -= 1
                elif self.up_button2.rect.collidepoint(event.pos):
                    if self.num_of_player + self.num_of_computer >= 6:
                        pass
                    else:
                        self.num_of_computer += 1
                elif self.down_button3.rect.collidepoint(event.pos):
                    if self.num_of_meeple == 0:
                        self.num_of_meeple = 0
                    else:
                        self.num_of_meeple -= 1
                elif self.up_button3.rect.collidepoint(event.pos):
                    if self.num_of_meeple >= 3:
                        pass
                    else:
                        self.num_of_meeple += 1
                elif self.next_button_up.rect.collidepoint(event.pos):
                    self.button_setting = False
                    self.screen_setting = False
                    self.screen_meeple = True
                    self.button_meeple = True
                    for i in range(self.num_of_player) :
                        self.screen_mee_list.append([]) # 플레이어 수만큼 리스트 추가

        # 화면 그리기
        self.player_text = self.game_font.render(str(self.num_of_player), True, (0, 0, 0))
        self.computer_text = self.game_font.render(str(self.num_of_computer), True, (0, 0, 0))
        self.meeple_num = self.game_font.render(str(self.num_of_meeple), True, (0, 0, 0))
        if self.button_setting:
            self.screen.blit(self.background.put_image("setting"), (0, 0))
            self.button_screen_blit(self.next_button_up)
            self.button_screen_blit(self.down_button1)
            self.button_screen_blit(self.up_button1)
            self.button_screen_blit(self.down_button2)
            self.button_screen_blit(self.up_button2)
            self.button_screen_blit(self.down_button3)
            self.button_screen_blit(self.up_button3)
            self.screen.blit(self.player_text, (735, 260))
            self.screen.blit(self.computer_text, (735, 385))
            self.screen.blit(self.meeple_num, (735, 540))
            self.init_text = self.num_of_player

    # 플레이어마다 게임말 선택
    def show_meeple_screen(self):
        # 이벤트 처리
        for event in pygame.event.get():
            # 창 닫기 누르면 끝 부분(ENDING_SCREEN)으로 넘어감
            if event.type == pygame.QUIT:
                self.screen_meeple = False
                self.screen_ending = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                temp = []
                # 플레이어 수만큼 이미지 선택 + player_list에 초기화
                for mee in self.meeple_button_list:
                    if mee.rect.collidepoint(event.pos) and self.init_text > 0:
                        self.init_text -= 1
                        self.player_list.append(Player.Player(self.num_of_meeple, mee.color))
                        self.computer_mee_list.remove(self.meeple_button_list.index(mee) + 1)
                        mee.set_void()

                # 시작버튼 누르면 중간부분(game_screen)의 보드판 화면으로 넘어감
                if self.next_button.rect.collidepoint(event.pos) and self.next_board:
                    self.button_meeple = False
                    self.screen_meeple = False
                    self.screen_game = True
                    self.button_board = True

        # 화면 그리기
        if self.button_meeple:
            self.screen.blit(self.background.put_image("meeple"), (0, 0))
            self.button_screen_blit(self.next_button)

            # 게임말들 화면에 차례대로 보이기
            for i, entity in enumerate(self.meeple_button_list):
                entity.x_pos = ((i+2) * self.screen_width / 9) - (entity.width / 2)
                entity.y_pos = (self.screen_height / 2) - (entity.height / 2)
                self.button_screen_blit(entity)
                entity.set_rect()

            if self.init_text == self.num_of_player:
                self.text_blit("player의 말을 골라주세요!", 255, 100, 100, self.screen_width / 2, 200)
            elif self.init_text != 0:
                self.text_blit(str(self.init_text) + "명 더 골라주세요!", 255, 100, 100, 540, 200)
            else :
                self.text_blit("말을 모두 골랐습니다! 다음으로 넘어가주세요.", 255, 100, 100, 540, 200)
                self.next_board = True
                if self.setcomputer :
                    com_mee_idx_list = random.sample(self.computer_mee_list, self.num_of_computer)
                    for mee in com_mee_idx_list:
                        self.computer_list.append(Computer.Computer(self.num_of_meeple, self.meeple_button_list[mee-1].color))
                    self.setcomputer = False

    def show_ending_screen(self):  # 엔딩화면 (재시작과 종료버튼을 다룸)
        # 간단한 이벤트 부분 (restart, end 버튼 클릭 이벤트)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen_ending = False  # 메인의 ending_screen while문을 빠져나감.
                self.running = False  # 메인의 running while문을 빠져나감.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 종료버튼을 누르면 게임이 종료됨.
                if self.end_button.rect.collidepoint(event.pos):
                    self.screen_ending = False
                    self.running = False
                # 다시시작 버튼을 누르면 시작부분(title_screen)의 시작화면으로 넘어감
                elif self.restart_button.rect.collidepoint(event.pos):
                    self.screen_ending = False; self.screen_title = True
                    self.button_home = True; self.button_help = False; self. button_board = False
                    self.button_table = False; self.button_green = False; self.push = False

        # 화면 출력 부분(끝배경, 종료버튼, 다시시작버튼)
        self.screen.blit(self.background.put_image("finish"), (0, 0))
        self.screen.blit(self.end_button.image,
                         (self.end_button.x_pos, self.end_button.y_pos))
        self.screen.blit(self.restart_button.image,
                         (self.restart_button.x_pos, self.restart_button.y_pos))

    def set_order(self):
        while len(self.computer_list)+len(self.player_list) != 0: # 컴퓨터 리스트의 길이와 플레이어 리스트의 길이의 합이 0 아니면
            i = random.randrange(2)
            if i == 0 and len(self.computer_list) != 0:
                print(len(self.computer_list))
                j = random.randrange(len(self.computer_list))
                self.order.append(self.computer_list[j])
                del self.computer_list[j]
            elif i == 1 and len(self.player_list) != 0:
                j = random.randrange(len(self.player_list))
                self.order.append(self.player_list[j])
                del self.player_list[j]
        for i in self.order:
            self.mee_button.append(Meeple.Meeple(i.meeples[self.num_of_meeple].color, sum=self.num_of_meeple))

    # 게임 로직: 메인 이벤트
    def main_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 종료
                self.screen_game = False
                self.screen_ending = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.next_button.rect.collidepoint(event.pos) and self.button_board: # 다음 버튼 눌렀을 때 보드판으로 이동
                    self.button_board = False
                    self.button_table = True
                # 그린 버튼 눌렀을 때 윷 돌리기
                if self.green_button.rect.collidepoint(event.pos) and self.button_table:
                    self.button_green = True
                    self.push = True
                # 우측 말 판 표시기
                for i, mee in enumerate(self.mee_button):
                    if mee.rect.collidepoint(event.pos) and self.button_board and self.order_idx == i and \
                            self.order[self.order_idx].board_num < self.num_of_meeple and \
                            len(self.screen_mee_list[self.order_idx]) != 0:
                        self.mee_button[i].minus_sum()
                        self.order[self.order_idx].board_num += 1
                        self.screen_mee_list[self.order_idx].append(
                            self.order[self.order_idx].meeples[self.order[self.order_idx].board_num])

            elif event.type == pygame.MOUSEBUTTONUP:  # 윷 돌리기
                self.push = False
            elif event.type == pygame.KEYDOWN:  # 키보드 입력
                if event.key == pygame.K_SPACE and self.button_table:
                    self.button_green = True
                    self.push = True
                if event.key == pygame.K_SPACE and self.button_board:
                    self.button_board = False
                    self.button_table = True
            elif event.type == pygame.KEYUP and self.button_table:
                self.push = False

    # 게임 화면(윷놀이가 진행될 때의 화면)
    def show_game_screen(self):
        if self.button_board:
            self.board_screen_blit()  # 보드판 화면 구현 함수
            if self.meeple_move:  # 윷을 던진 결과를 보드에 적용
                self.move_meeple()
                self.meeple_move = False

        elif self.button_table:  # 윷 테이블로 이동하기 버튼 눌렀을 때
            self.screen.blit(self.background.put_image("table"), (0, 0))
            self.screen.blit(self.green_button.image,
                             (self.green_button.x_pos, self.green_button.y_pos))
            self.yut.display_yut()
            self.text_blit("버튼을 한번만 누르세요", 250, 250, 250, 540, 680)
            if self.button_green:  # 윷 던지기(스페이스바)를 눌렀을 때
                if self.push:  # 스페이스바를 누르고 있을 때 윷 애니메이션 작동
                    self.button()
                    self.motion_update(60)
                else:  # 스페이스바를 뗐을 때 결과 출력
                    self.main_delay(1)  # 윷 결과 1초동안 보여주기
                    self.yut_rst = self.yut.result()
                    self.button_table = False
                    self.button_board = True
                    self.button_green = False
                    self.meeple_move = True

    def board_screen_blit(self):  # 보드 화면 출력
        self.yut.yut_state_reset()  # 윷을 모두 앞으로 리셋
        self.screen.blit(self.background.put_image("board"), (0, 0))
        self.screen.blit(self.next_button.image,
                         (self.next_button.x_pos, self.next_button.y_pos))
        self.screen.blit(self.yut_board.image,
                         (self.yut_board.x_pos, self.yut_board.y_pos))
        for i, player_mee in enumerate(self.order):
            self.text_blit("{}번".format(i + 1), 0, 0, 0, 855, 45 + 90 * i)
            self.mee_button[i].set_pos(945, 45+90*i)
            self.meeple_screen_blit(self.mee_button[i])
        if self.order_idx >= len(self.order):
            self.order_idx = 0
        self.text_blit("<-", 255, 0, 0, 1035, 45+90*self.order_idx)
        for screen_player in self.screen_mee_list:  # 보드판 위 말 화면에 출력
            for screen_mee in screen_player:
                self.meeple_screen_blit(screen_mee)
        if len(self.screen_mee_list[self.order_idx]) != 0:
            self.meeple_screen_blit(self.screen_mee_list[self.order_idx][0])

    def button_screen_blit(self, button):  # 버튼 화면에 표시 함수
        self.screen.blit(button.image, (button.x_pos, button.y_pos))

    def text_blit(self, text, r, g, b, x, y):  # 텍스트 출력 함수
        text_render = self.game_font.render(text, True, (r, g, b))
        text_rect = text_render.get_rect().size
        text_width = text_rect[0]
        text_height = text_rect[1]
        self.screen.blit(text_render, (x - text_width / 2, y - text_height / 2))

    def meeple_screen_blit(self, mee):  # 말 화면에 나타내기 함수
        self.screen.blit(mee.image, (mee.x_pos - mee.width/2, mee.y_pos - mee.height/2))

    def main_delay(self, sec):  # 딜레이 함수

        temp_ticks = pygame.time.get_ticks()
        while (pygame.time.get_ticks() - temp_ticks <= sec*1000) :
            self.screen.blit(self.background.put_image("table"), (0, 0))
            self.screen.blit(self.red_button.image,
                             (self.red_button.x_pos, self.red_button.y_pos))
            self.text_blit("참 잘했어요^^", 250, 250, 250, 540, 680)
            self.yut.display_yut()
            self.yut.result()
            pygame.display.update()

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

    def move_meeple_sec(self, move, mee):  # 한 칸씩 움직이기
        for i in range(move):
            temp_ticks = pygame.time.get_ticks()
            while pygame.time.get_ticks() - temp_ticks <= 500:
                self.board_screen_blit()
                pygame.display.update()
            mee.move(1)

    def move_meeple(self):  # 화면상에서 말 움직이기 함수
        if self.order[self.order_idx].board_num == 0:
            self.screen_mee_list[self.order_idx].append(self.order[self.order_idx].meeples[1])
            self.order[self.order_idx].board_num += 1
            self.meeple_screen_blit(self.screen_mee_list[self.order_idx][0])
            self.mee_button[self.order_idx].minus_sum()

        if self.yut_rst == 1:
            self.move_meeple_sec(1, self.order[self.order_idx].meeples[1])
            self.order_idx += 1
        elif self.yut_rst == 2:
            self.move_meeple_sec(2, self.order[self.order_idx].meeples[1])
            self.order_idx += 1
        elif self.yut_rst == 3:
            self.move_meeple_sec(3, self.order[self.order_idx].meeples[1])
            self.order_idx += 1
        elif self.yut_rst == 4:
            self.move_meeple_sec(4, self.order[self.order_idx].meeples[1])
        elif self.yut_rst == 0:
            self.move_meeple_sec(5, self.order[self.order_idx].meeples[1])


if __name__ == "__main__":
    test = YutGame()
    print(test.computer_list)
