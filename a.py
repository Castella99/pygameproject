board_map = [
    (602, 603), (607, 495), (608, 382), (605, 270), (604, 160), (603, 52),   # 00 01 02 03 04 05
    (490, 47), (377, 50), (267, 49), (151, 51), (40, 50), (39, 159),         # 06 07 08 09 10 11
    (42, 273), (42, 383), (39, 494), (42, 610), (151, 611), (264, 610),      # 12 13 14 15 16 17
    (379, 608), (488, 608), (513, 138), (425, 221), (323, 323), (239, 408),  # 18 19 20 21 22 23
    (150, 493), (141, 152), (236, 239), (323, 323), (407, 415), (503, 510),  # 24 25 26 27 28 29
    (600, 605)
]

print("[")
for i in board_map:
    i = list(i)
    i[0] += 145
    i[1] += 45
    print("({}, {})".format(i[0], i[1]), end=", ")
print("]")



board_map = [
    (602, 603), (607, 495), (608, 382), (605, 270), (604, 160), (603, 52),   # 00 01 02 03 04 05
    (490, 47), (377, 50), (267, 49), (151, 51), (40, 50), (39, 159),         # 06 07 08 09 10 11
    (42, 273), (42, 383), (39, 494), (42, 610), (151, 611), (264, 610),      # 12 13 14 15 16 17
    (379, 608), (488, 608), (513, 138), (425, 221), (323, 323), (239, 408),  # 18 19 20 21 22 23
    (150, 493), (141, 152), (236, 239), (323, 323), (407, 415), (503, 510),  # 24 25 26 27 28 29
    (600, 605)
]

# 게임 스크린에 맞도록 보드칸 위치 값 수정
for x in range(len(board_map)):
    board_map[x] = list(board_map[x])
    board_map[x][0] += 165
    board_map[x][1] += 68
    board_map[x] = tuple(board_map[x])





class test:
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
                player.meeples[player.idx].change_sum_and_image()
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