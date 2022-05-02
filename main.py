import YutGame
import pygame

game = YutGame.YutGame()

while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game.start_button.rect.collidepoint(event.pos) and game.start_background:
                game.start = True  # 보드판으로 이동
            elif game.help_button.rect.collidepoint(event.pos) and game.start_background:
                game.help = True  # 규칙 설명으로 이동
            elif game.home_button.rect.collidepoint(event.pos) and game.help_background:
                game.home = True  # 시작 화면으로 이동
            elif game.red_button.rect.collidepoint(event.pos) and game.table_background:
                game.red = True  # 보드판으로 이동
            elif game.next_button.rect.collidepoint(event.pos) and game.board_background:
                game.next = True  # 테이블로 이동
            elif game.restart_button.rect.collidepoint(event.pos) and game.restart_button:
                game.restart = True  # 시작 화면으로 이동
            elif game.end_button.rect.collidepoint(event.pos) and game.end_button:
                game.running = False  # 게임 종료
        elif event.type == pygame.MOUSEBUTTONUP:
            game.start = game.help = game.home = False
            game.red = game.next = game.restart = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.green = True
                game.push = game.button()  # 윷 던지기
        elif event.type == pygame.KEYUP:
            game.green = False
        game.show_Background_and_Button()
        pygame.display.update()
pygame.quit()

