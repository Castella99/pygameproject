import YutGame
import pygame

game = YutGame.YutGame()

while game.running:
# 게임 파트를 3개로 나눔(시작과 도움말, 보드판과 윷판, 엔딩 화면)
    while game.title_screen:  # 시작 부분
        game.show_title_screen()  # 시작부분 이벤트와 화면그리기 (게임 초기 설정 추가 예정)
        pygame.display.update()
    
    while game.setting_screen : # 세팅 화면 구현
        game.show_setting_screen()
        pygame.display.update()

        
pygame.quit()

