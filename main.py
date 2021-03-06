import YutGame
import pygame

game = YutGame.YutGame()

while game.running:
    # 게임 파트를 4개로 나눔(시작과 도움말, 초기 설정, 보드판과 윷판, 엔딩 화면)
    # 시작 부분
    while game.title_screen:
        game.show_title_screen()  # 시작부분 이벤트와 화면그리기 (게임 초기 설정 추가 예정)
        pygame.display.update()

    # 세팅 화면 구현
    while game.setting_screen:
        game.show_setting_screen()
        pygame.display.update()
    # 게임말 선택 화면
    while game.meeple_screen:
        game.show_meeple_screen()
        pygame.display.update()

    # 중간 부분
    while game.game_screen:
        game.main_events()  # 게임 이벤트 (게임 말 이동, 플레이어 순서 추가 예정)
        game.check()  # 승패 체크(미구현)
        game.show_game_screen()  # 화면그리기 (보드판, 게임 말 추가예정)
        pygame.display.update()

    # 끝 부분
    while game.ending_screen:
        game.show_ending_screen()  # 끝 부분 이벤트와 화면그리기 (승자 패자 화면 출력 추가 예정)
        pygame.display.update()

pygame.quit()

