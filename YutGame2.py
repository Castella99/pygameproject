import Arrow
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

        # 세팅에 필요한 변수들
        self.player_text = None
        self.computer_text = None
        self.meeple_num = None

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
        self.num_of_player = 0
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
        self.order_idx = 0  # 현재 순번의 말
        self.yut_rst = 0  # 윳 던진 결과
        self.screen_mee_list = []  # 스크린상에 표시되어야할 말
        self.mee_button = []
        self.winner = "아직 안 정해짐"

        pygame.display.set_caption("yut Game")
        self.background = Background.Background("start")  # 배경 객체

        # 게임 진행 로직에 필요한 변수
        self.is_gp1 = True  # 게임 보드 화면: next 버튼을 눌러 윷화면으로 이동 (-> gp2)
        self.is_gp2 = False  # 게임 윷 화면: green버튼을 눌러 윷을 던짐 그리고 보드 화면으로 다시 이동 (-> gp4)
        self.is_gp3 = False  # 게임 보드 화면: 이동시킬 말 선택 (-> gp4)
        self.is_gp4 = False  # 게임 보드 화면: 윷의 결과만큼 말을 이동 (-> gp5)
        self.is_gp5 = False  # 게임 보드 화면: 한번 더 할 지 턴을 넘길지 결정(break or -> gp2)
        # base: p1 -> p2 -> p3 -> p4 -> p5 -> break
        # case2: 한번더 하는 경우           ㄴ> p2 -> p3 -> p4 -> p5
        self.is_again = False

        # 윷과 윷판 객체
        self.yut = Yut.Yut("front", 1)
        self.yut_board = gameBoard.GameBoard()

        self.animation_time = round(100 / len(self.yut.yut_images * 100), 2)

        # 각종 버튼 객체
        self.start_button = Button.Button("start button", 1, 2, 2, 3)
        self.help_button = Button.Button("help button", 1, 2, 7, 8)
        self.home_button = Button.Button("home button", 8, 10, 1, 6)
        self.red_button = Button.Button("red button", 1, 2, 9, 11)
        self.green_button = Button.Button("green button", 1, 2, 9, 11)
        self.next_button = Button.Button("next button", 8, 9, 9, 10)
        self.next_button_up = Button.Button("next button", 8, 9, 1, 7)
        self.restart_button = Button.Button("restart button", 1, 2, 2, 3)
        self.end_button = Button.Button("end button", 1, 2, 7, 8)
        self.down_button1 = Button.Button("down button", 7, 12, 3, 8)
        self.up_button1 = Button.Button("up button", 4, 5, 3, 8)
        self.down_button2 = Button.Button("down button", 7, 12, 5, 9)
        self.up_button2 = Button.Button("up button", 4, 5, 5, 9)
        self.down_button3 = Button.Button("down button", 7, 12, 7, 9)
        self.up_button3 = Button.Button("up button", 4, 5, 7, 9)

        # 이동 방향 객체
        self.arrow = [
            Arrow.Arrow("up", Arrow.arrow_map[1]), Arrow.Arrow("left", Arrow.arrow_map[6]),
            Arrow.Arrow("leftdown", Arrow.arrow_map[20]), Arrow.Arrow("down", Arrow.arrow_map[11]),
            Arrow.Arrow("rightdown", Arrow.arrow_map[25]), Arrow.Arrow("right", Arrow.arrow_map[16]),
            Arrow.Arrow("rightup", Arrow.arrow_map[24]), Arrow.Arrow("leftup", Arrow.arrow_map[26]),
            Arrow.Arrow("rightdown", Arrow.arrow_map[28]), Arrow.Arrow("leftdown", Arrow.arrow_map[23])
        ]

        for color in self.meeple_color_list:
            self.meeple_button_list.append(Meeple.Meeple(color, 0, 0, 0))



    def __del__(self):
        print("게임이 제거 되었습니다.")

    # 버튼 화면에 표시 함수
    def button_screen_blit(self, button):
        self.screen.blit(button.image, (button.x_pos, button.y_pos))

    # 텍스트 출력 함수
    def text_blit(self, text, RGB, x, y):
        text_render = self.game_font.render(text, True, (RGB[0], RGB[1], RGB[2]))
        text_rect = text_render.get_rect().size
        text_width = text_rect[0]
        text_height = text_rect[1]
        self.screen.blit(text_render, (x - text_width / 2, y - text_height / 2))

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
                # 사람의 수 결정
                if self.down_button1.rect.collidepoint(event.pos):
                    if self.num_of_player == 0:
                        self.num_of_player = 0
                    else:
                        self.num_of_player -= 1
                elif self.up_button1.rect.collidepoint(event.pos):
                    if self.num_of_player + self.num_of_computer >= 6:
                        pass
                    else:
                        self.num_of_player += 1
                # 컴퓨터의 수 설정
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
                # 게임말 개수 설정
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
                # meeple 색 결정하는 화면으로 넘어감
                elif self.next_button_up.rect.collidepoint(event.pos):
                    self.button_setting = False
                    self.screen_setting = False
                    if self.num_of_player == 0:
                        self.screen_game = True
                        self.button_board = True
                        com_mee_idx_list = random.sample(self.computer_mee_list, self.num_of_computer)
                        for mee in com_mee_idx_list:
                            self.computer_list.append(
                                Computer.Computer(self.num_of_meeple, self.meeple_button_list[mee - 1].color))
                        self.setcomputer = False
                    else:
                        self.screen_meeple = True
                        self.button_meeple = True
                    for i in range(self.num_of_player):
                        self.screen_mee_list.append([])  # 플레이어 수만큼 리스트 추가
                    for i in range(self.num_of_computer):
                        self.screen_mee_list.append([])  # 플레이어 수만큼 리스트 추가
                    # 필요없는 메모리 절약
                    del self.up_button1
                    del self.up_button2
                    del self.up_button3
                    del self.down_button1
                    del self.down_button2
                    del self.down_button3
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

                # 시작버튼 누르면 game_screen의 보드판 화면으로 넘어감
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
                self.text_blit("player의 말을 골라주세요!", (255, 100, 100), self.screen_width / 2, 200)
            elif self.init_text != 0:
                self.text_blit(str(self.init_text) + "명 더 골라주세요!", (255, 100, 100), 540, 200)
            else:
                self.text_blit("말을 모두 골랐습니다! 다음으로 넘어가주세요.", (255, 100, 100), 540, 200)
                self.next_board = True
                if self.setcomputer :
                    com_mee_idx_list = random.sample(self.computer_mee_list, self.num_of_computer)
                    for mee in com_mee_idx_list:
                        self.computer_list.append(Computer.Computer(self.num_of_meeple, self.meeple_button_list[mee-1].color))
                    self.setcomputer = False

    # 엔딩 화면
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
                    self.screen_ending = False

        # 화면 출력 부분(끝배경, 종료버튼, 다시시작버튼)
        victory_text = "우승자는 " + self.winner + "!!!"
        self.screen.blit(self.background.put_image("finish"), (0, 0))
        self.screen.blit(self.end_button.image,
                         (self.end_button.x_pos, self.end_button.y_pos))
        self.screen.blit(self.restart_button.image,
                         (self.restart_button.x_pos, self.restart_button.y_pos))
        self.text_blit(victory_text, (0, 0, 0), 540, 100)
        no_winner = True
        for i in self.order:
            if i.state == 1:
                self.screen.blit(i.meeples[0].image,(720, 70))
                no_winner = False
        if no_winner:
            self.screen.blit(Meeple.Meeple.mipple_images["void"][1], (770, 70))

    # player 순서를 랜덤으로 정함.
    def set_order(self):
        # 컴퓨터 리스트의 길이와 플레이어 리스트의 길이의 합이 0 아니면
        while len(self.computer_list)+len(self.player_list) != 0:
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
        # 보드 옆에 둘 게임말 상태창 리스트 초기화
        for i in self.order:
            self.mee_button.append(Meeple.Meeple(i.meeples[self.num_of_meeple-1].color, sum=0))

    # 보드 화면 출력
    def board_screen_blit(self, player):
        idx = self.order.index(player)
        self.yut.yut_state_reset()  # 윷을 모두 앞으로 리셋
        self.screen.blit(self.background.put_image("board"), (0, 0))
        self.screen.blit(self.next_button.image,
                         (self.next_button.x_pos, self.next_button.y_pos))
        self.screen.blit(self.yut_board.image,
                         (self.yut_board.x_pos, self.yut_board.y_pos))

        # 보드판 옆에 게임 상태 보여주기
        for i, player_mee in enumerate(self.order):
            self.text_blit("{}번".format(i + 1), (0, 0, 0), 855, 45 + 90 * i)
            self.mee_button[i].set_pos(945, 45 + 90 * i)
            self.meeple_screen_blit(self.mee_button[i])
        self.text_blit("<-", (255, 0, 0), 1035, 45 + 90 * idx)

        # 보드판 위 말 화면에 출력: meeple의 상태가 1인것만 화면에 출력
        for player in self.order:
            for meeple in player.meeples:
                if meeple.state == 2:
                    continue
                if meeple.state == 1:
                    self.meeple_screen_blit(meeple)

        # 이동가능한 화살표 표시
        if self.is_gp3:
            self.show_arrow()

    # 가능한 arrow 모두 표시
    def show_arrow(self):
        for arrow in self.arrow:
            if arrow.state:
                self.screen.blit(arrow.image, (arrow.x_pos, arrow.y_pos))

    # 말 화면에 나타내기 함수
    def meeple_screen_blit(self, mee):
        self.screen.blit(mee.image, (mee.x_pos - mee.width / 2, mee.y_pos - mee.height / 2))

    def game_process(self, player):
        #승패가 결정됨.
        if player.check_done():
            if player.state != 0:
                print("이미 순위가 결정됨.")
                return True
            player.state = Player.Player.score
            Player.Player.score += 1
            print("순위를 매김", str(player.state)+"등, 다음은", Player.Player.score)
            return True
        # 아직 남음
        else:
            if self.is_gp1:
                self.process1(player)
            elif self.is_gp2:
                self.process2(player)
            elif self.is_gp3:
                self.process3(player)
            elif self.is_gp4:
                if self.process4(player) == "finish":
                    self.print_all_state()
                    return True
            elif self.is_gp5:
                prompt = self.process5(player)
                if prompt == "finish":
                    return True
            pygame.display.update()

    # 게임 첫 화면: 윷 화면으로 넘어간다.
    def process1(self, player):
        # 사용자 이벤트

        self.board_screen_blit(player)
        for event in pygame.event.get():
            # 종료
            if event.type == pygame.QUIT:
                self.screen_game = False
                self.screen_ending = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(self.next_button.rect, event.pos)
                # 다음 버튼 눌렀을 때 보드판으로 이동
                if self.next_button.rect.collidepoint(event.pos):
                    self.is_gp1 = False
                    self.is_gp2 = True
            elif event.type == pygame.KEYDOWN:  # 키보드 입력
                # 스페이스바 눌러도 보드판으로 이동
                if event.key == pygame.K_SPACE:
                    self.is_gp1 = False
                    self.is_gp2 = True
        # 컴퓨터가 하는 중
        if type(player) is Computer.Computer:
            sec = 0.5
            temp_ticks = pygame.time.get_ticks()
            while pygame.time.get_ticks() - temp_ticks <= sec * 1000:
                self.board_screen_blit(player)
                self.text_blit("컴퓨터가 하는 중...", Computer.Computer.color_list[player.color], 180, 40)
                pygame.display.update()
            self.is_gp1 = False
            self.is_gp2 = True

    # 윷 던지기
    def process2(self, player):
        # 사용자 이벤트
        if type(player) is Player.Player:
            self.table_screen_blit(player)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen_game = False
                    self.screen_ending = True
                    self.is_gp2 = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.green_button.rect.collidepoint(event.pos):
                        self.button_green = True
                        self.push = True
                elif event.type == pygame.MOUSEBUTTONUP:  # 윷 돌리기
                    self.push = False
                elif event.type == pygame.KEYDOWN:  # 키보드 입력
                    if event.key == pygame.K_SPACE:
                        self.button_green = True
                        self.push = True
                elif event.type == pygame.KEYUP:
                    self.push = False
        # 컴퓨터가 하는 중
        else:
            sec = 0.5
            temp_ticks = pygame.time.get_ticks()
            self.button_green = True
            self.push = True
            while pygame.time.get_ticks() - temp_ticks <= sec * 1000:
                self.table_screen_blit(player)
                pygame.display.update()
            self.push = False
            self.table_screen_blit(player)
        self.reset_arrow_idx()

    def table_screen_blit(self, player):
        self.screen.blit(self.background.put_image("table"), (0, 0))
        self.screen.blit(self.green_button.image,
                         (self.green_button.x_pos, self.green_button.y_pos))
        self.yut.display_yut()
        self.text_blit("버튼을 한번만 누르세요", (250, 250, 250), 540, 680)
        # 윷 던지기(스페이스바)를 눌렀을 때
        if self.button_green:
            # 스페이스바를 누르고 있을 때 윷 애니메이션 작동
            if self.push:
                if type(player) is Computer.Computer:
                    self.text_blit("컴퓨터가 하는 중...", Computer.Computer.color_list[player.color], 180, 40)
                self.button()
                self.motion_update(60)
            # 스페이스바를 뗐을 때 결과 출력
            else:
                # 윷 결과 1.5초동안 보여주기
                self.main_delay(1.5, player)
                self.yut_rst = self.yut.result()
                self.button_green = False
                self.is_gp2 = False
                self.is_gp3 = True

    def button(self):  # 윷 던지기(윷의 상태를 랜덤으로 생성 함)
        self.yut.yut_state.clear()  # 윷 상태 리스트 초기화
        for i in range(4):  # 윷 상태 만들기
            self.yut.yut_state.append(random.randrange(0, 1 +1))  # 0, 1을 랜덤으로 받아서 추가
        #print(self.yut.yut_state)

    def motion_update(self, mt):  # 윷이 돌아가는 애니메이션(수정 할 계획)
        self.current_time += mt
        # 시간을 늦추는 역할?
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index += 1
            # 윷 사진의 인덱스를 넘어가면 0으로 초기화
            if self.index >= len(self.yut.yut_images):
                self.index = 0
            self.yut.image = self.yut.yut_images[self.index]  # 윷의 이미지는 앞, 우, 뒤, 좌로 돌아감
            self.yut.display_yut()  # 윷 4개 화면에 출력

    # 윷을 던지고 난 후 애니메이션
    def main_delay(self, sec, player):
        temp_ticks = pygame.time.get_ticks()
        while pygame.time.get_ticks() - temp_ticks <= sec*1000:
            self.screen.blit(self.background.put_image("table"), (0, 0))
            self.screen.blit(self.red_button.image,
                             (self.red_button.x_pos, self.red_button.y_pos))
            self.text_blit("참 잘했어요^^", (250, 250, 250), 540, 680)
            self.yut.display_yut()
            self.yut.result()
            # 컴퓨터가 하는 중
            if type(player) is Computer.Computer:
                self.text_blit("컴퓨터가 하는 중...", Computer.Computer.color_list[player.color], 180, 40)
            pygame.display.update()

    def reset_arrow_idx(self):
        for arrow in self.arrow:
            arrow.who = 0
            arrow.state = False

    # 어떤 게임말 어디로 이동할지 선택
    def process3(self, player):
        self.board_screen_blit(player)
        # 가능한 화살표 다 보이기
        for idx in range(player.num):
            if player.meeples[idx].state == 0 or player.meeples[idx].state == 1:
                if player.meeples[idx].pos == 0:
                    if player.check_state():
                        pass
                    else:
                        self.arrow[0].set_arrow(True,idx)
                elif player.meeples[idx].pos == 5:
                    self.arrow[1].set_arrow(True,idx)
                    self.arrow[2].set_arrow(True, idx)
                elif player.meeples[idx].pos == 10:
                    self.arrow[3].set_arrow(True,idx)
                    self.arrow[4].set_arrow(True, idx)
                elif player.meeples[idx].pos == 15:
                    self.arrow[5].set_arrow(True,idx)
                elif player.meeples[idx].pos == 22:
                    self.arrow[7].set_arrow(True,idx)
                    self.arrow[8].set_arrow(True, idx)
                    self.arrow[9].set_arrow(True, idx)
                elif player.meeples[idx].pos == 27:
                    self.arrow[8].set_arrow(True,idx)

        #사용자 이벤트
        if type(player) is Player.Player:
            for event in pygame.event.get():
                # 종료
                if event.type == pygame.QUIT:
                    self.screen_game = False
                    self.screen_ending = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # 화살표를 누른 경우
                    for arrow in self.arrow:
                        #print("커서:", event.pos, "화살표 위치:", arrow.rect)
                        if arrow.rect.collidepoint(event.pos) and arrow.state:
                            player.idx = arrow.who
                            # 고른 것만 true로 만들기
                            for i in self.arrow:
                                i.state = False
                            self.arrow[self.arrow.index(arrow)].state = True
                            self.is_gp3 = False
                            self.is_gp4 = True
                            break
                    # 게임말을 누른 경우
                    for meeple in player.meeples:
                        if meeple.state == 2:
                            continue
                        meeple.set_left_top()
                        #print("커서:", event.pos, "게임말 위치:", meeple.rect)
                        if meeple.state == 1 and meeple.rect.collidepoint(event.pos):
                            player.idx = player.meeples.index(meeple)
                            # arrow 모두 false로 만들기
                            for i in self.arrow:
                                i.state = False
                            self.is_gp3 = False
                            self.is_gp4 = True

        # 컴퓨터가 하는 중
        else:
            self.choose_arrow(player)

    def choose_arrow(self, player):
        temp_list = []
        # 만약 지름길을 고를 수 있으면 무조건 고름.
        for meeple in player.meeples:
            if meeple.state == 2:
                continue
            if meeple.pos == 22:
                player.idx = player.meeples.index(meeple)
                for arrow in self.arrow:
                    arrow.state = False
                self.arrow[8].state = True
                self.is_gp3 = False
                self.is_gp4 = True
                return
            elif meeple.pos == 5:
                player.idx = player.meeples.index(meeple)
                for arrow in self.arrow:
                    arrow.state = False
                self.arrow[2].state = True
                self.is_gp3 = False
                self.is_gp4 = True
                return
            elif meeple.pos == 10:
                player.idx = player.meeples.index(meeple)
                for arrow in self.arrow:
                    arrow.state = False
                self.arrow[4].state = True
                self.is_gp3 = False
                self.is_gp4 = True
        # 아니면 내가 있는 위치에서 갈 수 있는 방향을 랜덤으로 감.
        for i in self.arrow:
            if i.state:
                temp_list.append(self.arrow.index(i))
            i.state = False
        # 정해져 있으면 그냥 정해진대로 감.
        if len(temp_list) == 0:
            for arrow in self.arrow:
                arrow.state = False
            # 움직일 meeple을 정함
            meeple_list = []
            for meeple in player.meeples:
                if meeple.state == 2:
                    continue
                if meeple.state == 1:
                    meeple_list.append(player.meeples.index(meeple))
            player.idx = random.choice(meeple_list)
            self.is_gp3 = False
            self.is_gp4 = True
            return
        # 침착하게 1초 기다림.
        sec = 0.5
        temp_ticks = pygame.time.get_ticks()
        while pygame.time.get_ticks() - temp_ticks <= sec * 1000:
            self.board_screen_blit(player)

            pygame.display.update()
        print(temp_list)
        for arrow in self.arrow:
            arrow.state = False
        arrow = random.choice(temp_list)
        self.arrow[arrow].state = True
        player.idx = self.arrow[arrow].who
        self.is_gp3 = False
        self.is_gp4 = True


    # 선택한 게임 말 이동하기
    def process4(self, player):
        # 윷을 던진 결과를 보드에 적용
        self.move_meeple(player)
        self.is_gp4 = False
        self.is_gp1 = True
        return "finish"

        # 사용자 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen_game = False
                self.screen_ending = True
                self.is_gp4 = False

    # 화면상에서 말 움직이기 함수; 윷의 결과만큼 이동시킴. + 업기 잡기 결정
    def move_meeple(self, player):
        # 현재 자기가 있는 칸은 -1로 바꿈
        print("움직이기 전:", self.yut_board.board_state)
        print("윷의 결과:",self.yut_rst)
        self.yut_board.board_state[player.meeples[player.idx].pos][0] = -1
        self.yut_board.board_state[player.meeples[player.idx].pos][1] = -1
        idx = self.order.index(player)
        #self.yut_rst = input("윷 결과를 입력하세요")
        if self.yut_rst == 1:
            self.move_meeple_sec(1, self.order[idx].meeples[player.idx], player)
        elif self.yut_rst == 2:
            self.move_meeple_sec(2, self.order[idx].meeples[player.idx], player)
        elif self.yut_rst == 3:
            self.move_meeple_sec(3, self.order[idx].meeples[player.idx], player)
        elif self.yut_rst == 4:
            self.move_meeple_sec(4, self.order[idx].meeples[player.idx], player)
        elif self.yut_rst == 0:
            self.move_meeple_sec(5, self.order[idx].meeples[player.idx], player)

    # 한 칸씩 움직이기; player의 움직일 meeple을 move만큼 이동시킴.
    def move_meeple_sec(self, move, mee, player):
        for i in range(move):
            temp_ticks = pygame.time.get_ticks()
            while pygame.time.get_ticks() - temp_ticks <= 500:
                self.board_screen_blit(player)
                if type(player) is Computer.Computer:
                    self.text_blit("컴퓨터가 하는 중...", Computer.Computer.color_list[player.color], 180, 40)
                pygame.display.update()
            mee.move(self.check_arrow())
            if mee.state == 2:
                break

    # 선택한 arrow가 무엇인지 확인
    def check_arrow(self):
        for i in self.arrow:
            if i.state:
                return self.arrow.index(i)
        return -1

        # 한번 더 할지 결정
    def process5(self, player):
        # 만약에 완주했으면 바로 턴 넘김.
        if player.check_done():
            print("완주해서 턴 넘김.")
            self.is_gp5 = False
            self.is_gp1 = True
            self.print_all_state()
            return "finish"
        self.board_screen_blit(player)
        idx = self.order.index(player)
        # who_this = 이동한 다음 자기(idx)가 올라간 위치.
        who_this = self.yut_board.board_state[player.meeples[player.idx].pos][0]
        this_meeple = self.yut_board.board_state[player.meeples[player.idx].pos][1]
        print(who_this, this_meeple)
        # 말들이 겹쳐질 때
        if who_this != -1:
            print("말 겹침")
            # 업을 수 있는 경우
            if who_this == idx and player.meeples[this_meeple].pos != 31:
                print("그래서 업음.")
                self.order[who_this].meeples[this_meeple].state = 3
                self.order[who_this].meeples[this_meeple].pos = 0
                player.meeples[player.idx].carry_my_back()
                # 턴 넘김
                self.yut_board.board_state[player.meeples[player.idx].pos][0] = idx
                self.yut_board.board_state[player.meeples[player.idx].pos][1] = player.idx
                print("움직이고 난 후:", self.yut_board.board_state)
                self.is_gp5 = False
                self.is_gp1 = True
                self.print_all_state()
                return "finish"
            # 잡을 수 있는 경우
            else:
                print("그래서 잡음")
                # 잡힌 게임 말의 상태와 위치는 0
                self.order[who_this].meeples[this_meeple].state = 0
                self.order[who_this].meeples[this_meeple].pos = 0
                # 업혀져 있는 게임 말들도 모두 0으로
                for meeple in self.order[who_this].meeples:
                    if meeple.state == 2:
                        continue
                    if meeple.state == 3:
                        self.order[who_this].meeples[this_meeple].state = 0
                        self.order[who_this].meeples[this_meeple].pos = 0
        # 말들이 겹치지 않았을 때
        else:
            print("말 안겹침")
            # 윷이나 모가 안 나오면 턴 넘김
            if 0 < self.yut_rst < 4:
                print("윷, 모 안 나옴")
                self.yut_board.board_state[player.meeples[player.idx].pos][0] = idx
                self.yut_board.board_state[player.meeples[player.idx].pos][1] = player.idx
                print("움직이고 난 후:", self.yut_board.board_state)
                self.is_gp5 = False
                self.is_gp1 = True
                self.print_all_state()
                return "finish"
            print("윷 모 나옴")
        self.yut_board.board_state[player.meeples[player.idx].pos][0] = idx
        self.yut_board.board_state[player.meeples[player.idx].pos][1] = player.idx
        self.is_gp5 = False
        self.is_gp1 = True
        print("움직이고 난 후:",self.yut_board.board_state)
        self.print_all_state()

        # 사용자 이벤트
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.screen_game = False
                self.screen_ending = True
                self.is_gp5 = False
    # 버그 수정에 사용 정신나갈거 같아~~
    def print_all_state(self):
        for i, player  in enumerate(self.order):
            print(str(i+1)+"번째 player:", player.state,end=", ")
            for j, meeple in enumerate(player.meeples):
                print(str(j+1)+"번째 말:",meeple.state,"-",meeple.pos, end=", ")
            print()

if __name__ == "__main__":
    pass