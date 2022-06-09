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
    path = os.path.dirname(os.path.abspath(__file__))

    running = True
    push = False

    # 각종 버튼 객체
    start_button = Button.Button("start button", 1, 2, 2, 3)
    help_button = Button.Button("help button", 1, 2, 7, 8)
    home_button = Button.Button("home button", 8, 10, 1, 6)
    red_button = Button.Button("red button", 1, 2, 6, 7)
    green_button = Button.Button("green button", 1, 2, 6, 7)
    next_button = Button.Button("next button", 8, 9, 6, 7)
    next_button_up = Button.Button("next button", 8, 9, 1, 7)
    restart_button = Button.Button("restart button", 1, 2, 2, 3)
    end_button = Button.Button("end button", 1, 2, 7, 8)
    down_button1 = Button.Button("down button", 7, 12, 3, 8)
    up_button1 = Button.Button("up button", 4, 5, 3, 8)
    down_button2 = Button.Button("down button", 7, 12, 5, 9)
    up_button2 = Button.Button("up button", 4, 5, 5, 9)
    down_button3 = Button.Button("down button", 7, 12, 7, 9)
    up_button3 = Button.Button("up button", 4, 5, 7, 9)

    # 현재 게임 상태가 어떤지 확인 하는 변수
    title_screen = True
    setting_screen = False
    meeple_screen = False
    game_screen = False
    ending_screen = False

    # 현재 어떤 버튼이 눌렸나 확인하는 변수들
    home = True
    help = False
    board = False
    table = False
    green = False
    setting = False
    meeple = False

    # 윷 돌아가는 에니메이션에 필요한 변수
    current_time = 0
    animation_index = 0
    animation_time = None

    # player 초기화에 필요한 변수
    #  초기 설정: 사람의 수와 컴퓨터의 수와 인당 가질 말의 수를 결정하는 변수 (컴퓨터 수와 사람의 수의 합은 6)
    num_of_player = 1
    num_of_computer = 0
    num_of_meeple = 1
    meeple_button_list = []

    init_text = 0
    next_board = False

    player_list = []
    computer_list = []
    computer_mee_list = [1, 2, 3, 4, 5, 6]
    setcomputer = True
    order = []  # 플레이어 총 순서

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

        meeple_color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        for color in meeple_color_list:
            self.meeple_button_list.append(Meeple.Meeple(color, 0))

    # 시작 화면 (규칙 설명으로 이동하고 다시 돌아 올 수 있음)
    def show_title_screen(self):
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

    # 플레이어 수, 게임말 개수 설정 화면
    def show_setting_screen(self):
        # 이벤트 처리
        for event in pygame.event.get():
            # 창 닫기 누르면 끝 부분(ENDING_SCREEN)으로 넘어감
            if event.type == pygame.QUIT:
                self.setting_screen = False
                self.ending_screen = True
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
                    self.setting = False
                    self.setting_screen = False
                    self.meeple_screen = True
                    self.meeple = True

        # 화면 그리기
        self.player_text = self.game_font.render(str(self.num_of_player), True, (0, 0, 0))
        self.computer_text = self.game_font.render(str(self.num_of_computer), True, (0, 0, 0))
        self.meeple_num = self.game_font.render(str(self.num_of_meeple), True, (0, 0, 0))
        if self.setting:
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
                self.meeple_screen = False
                self.ending_screen = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                temp = []
                # 플레이어 수만큼 이미지 선택 + player_list에 초기화
                for mee in self.meeple_button_list:
                    if mee.rect.collidepoint(event.pos):
                        self.init_text -= 1
                        self.player_list.append(Player.Player(self.num_of_meeple, mee.color))
                        print(self.meeple_button_list.index(mee))
                        self.computer_mee_list.remove(self.meeple_button_list.index(mee) + 1)
                        mee.set_void()

                # 시작버튼 누르면 중간부분(game_screen)의 보드판 화면으로 넘어감
                if self.next_button.rect.collidepoint(event.pos) and self.next_board:
                    self.meeple = False
                    self.meeple_screen = False
                    self.game_screen = True
                    self.board = True

        # 화면 그리기
        if self.meeple:
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
            elif self.setcomputer:
                self.text_blit("말을 모두 골랐습니다! 다음으로 넘어가주세요.", 255, 100, 100, 540, 200)
                self.next_board = True
                com_mee_idx_list = random.sample(self.computer_mee_list, self.num_of_computer)
                for mee in com_mee_idx_list:
                    self.computer_list.append(Computer.Computer(self.num_of_meeple, self.meeple_button_list[mee-1].color))
                    self.setcomputer = False

#-----------------------------------------------------------------------------------------------------
    def logic(self):
        next_turn = False
        while len(self.order) != 1:
            for player in self.order:
                while not next_turn:
                    if player.state != 0:
                        continue
                    player.throw_yut()

#-----------------------------------------------------------------------------------------------------
    # 게임 화면(윷놀이가 진행될 때의 화면)
    def show_game_screen(self):
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
                self.throw_yut()
                self.motion_update(60)
            else:  # 스페이스바를 뗐을 때 결과 출력
                self.yut.display_yut()
                self.screen.blit(self.red_button.image,
                                 (self.red_button.x_pos, self.red_button.y_pos))

    def set_order(self):
        while len(self.computer_list)+len(self.player_list) != 0:
            i = random.randrange(2)
            if i == 0 and len(self.computer_list) != 0:
                j = random.randrange(len(self.computer_list))
                self.order.append(self.computer_list[j])
                del self.computer_list[j]
            elif i == 1 and len(self.player_list) != 0:
                j = random.randrange(len(self.computer_list))
                self.order.append(self.player_list[j])
                del self.player_list[j]

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

    # 승패가 갈렸는지 확인 (미구현 상태)
    def check(self):
        pass
        # if 승패가 나면:
        #   self.game_screen = False
        #   self.ending_screen = True

    # 윷 던지기(윷의 상태를 랜덤으로 생성 함)
    def throw_yut(self):
        self.yut.yut_state.clear()  # 윷 상태 리스트 초기화
        for i in range(4):  # 윷 상태 만들기
            self.yut.yut_state.append(random.randrange(0, 1 + 1))  # 0, 1을 랜덤으로 받아서 추가
        print(self.yut.yut_state)

    # 윷이 돌아가는 애니메이션(수정 할 계획)
    def motion_update(self, mt):
        self.current_time += mt
        print(self.current_time, self.animation_time)
        # 시간을 늦추는 역할?
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.animation_index += 1
            # 윷 사진의 인덱스를 넘어가면 0으로 초기화
            if self.animation_index >= len(self.yut.yut_images):
                self.animation_index = 0
            self.yut.image = self.yut.yut_images[self.animation_index]  # 윷의 이미지는 앞, 우, 뒤, 좌로 돌아감
            self.yut.display_yut()  # 윷 4개 화면에 출력

    # 엔딩화면 (재시작과 종료버튼을 다룸) (추가 예정)
    def show_ending_screen(self):
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

    # 버튼 화면에 보이기
    def button_screen_blit(self, button):
        self.screen.blit(button.image, (button.x_pos, button.y_pos))

    # 텍스트 화면에 보이기
    def text_blit(self, text, r, g, b, x, y):
        text_render = self.game_font.render(text, True, (r, g, b))
        text_rect = text_render.get_rect().size
        text_width = text_rect[0]
        text_height = text_rect[1]
        self.screen.blit(text_render, (x - text_width / 2, y - text_height / 2))


if __name__ == "__main__":
    test = YutGame()
    print(test.computer_list)
