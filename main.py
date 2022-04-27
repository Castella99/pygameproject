import Yut
import pygame

yut = Yut.YutGame()
while yut.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yut.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                yut.push = yut.button()
        if event.type == pygame.KEYUP:
            yut.push = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            yut.push = yut.button()
        if event.type == pygame.MOUSEBUTTONUP:
            yut.push = False
    yut.redraw()
    pygame.display.update() #게임 화면을 다시 그리기
pygame.quit()