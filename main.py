import Yut
import pygame

yut = Yut.YutGame()
while yut.start :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yut.start = False
            yut.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                yut.start = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            yut.start = False
    yut.screen.blit(yut.background[0], (0,0))
    pygame.display.update()
    
while yut.running :
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