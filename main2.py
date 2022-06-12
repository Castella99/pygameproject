import Player
import YutGame2
import pygame


while True:
    game = YutGame2.YutGame()
    # 게임 파트를 4개로 나눔(시작과 도움말, 초기 설정, 보드판과 윷판, 엔딩 화면)
    # 시작 부분
    while game.screen_title:
        game.show_title_screen()  # 시작부분 이벤트와 화면그리기 (게임 초기 설정 추가 예정)
        pygame.display.update()

    # 세팅 화면 구현
    while game.screen_setting:
        game.show_setting_screen()
        pygame.display.update()

    # 게임말 선택 화면
    while game.screen_meeple:
        game.show_meeple_screen()
        pygame.display.update()

    # 게임 중
    game.set_order()  # 게임 순서 정하기
    while game.screen_game:
        is_finish = 0
        for player in game.order:
            print("player"+str(1 + game.order.index(player)))
            while True:
                is_stop = game.game_process(player)
                if is_stop:
                    break
                elif not game.screen_game:
                    break
            if not game.screen_game:
                break
        # 플레이어가 모두 빠져나왔을때 (All player.state != 0)
        for player in game.order:
            if player.state != 0:
                is_finish += 1
            if player.state == 1:
                game.winner = "player" + str(game.order.index(player)+1)
        if is_finish >= len(game.order)-1 and len(game.order) != 1:
            game.screen_ending = True
            game.screen_game = False
        elif len(game.order) == 1 and is_finish == len(game.order):
            game.screen_ending = True
            game.screen_game = False

    # 끝 부분
    for p in game.order:
        print("player"+ str(game.order.index(p)+1) +"은", p.state, "등")
    while game.screen_ending:
        game.show_ending_screen()  # 끝 부분 이벤트와 화면그리기 (승자 패자 화면 출력 추가 예정)
        pygame.display.update()
    if not game.running:
        break
    del game
    Player.Player.score = 0
pygame.quit()

