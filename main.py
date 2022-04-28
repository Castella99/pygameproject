import Yut
import pygame

yut = Yut.YutGame()
while yut.start :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            yut.start = False
            yut.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if yut.startButton_rect.collidepoint(event.pos) :
                yut.start = False
            elif yut.helpButton_rect.collidepoint(event.pos) :
                while yut.help :
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            yut.start = False
                            yut.running = False
                        elif event.type == pygame.MOUSEBUTTONDOWN :
                            if yut.homeButton_rect.collidepoint(event.pos) :
                                yut.help = False
                    yut.screen.blit(yut.background[2], (0,0))
                    yut.screen.blit(yut.homeButton, (yut.homeButton_x_pos, yut.homeButton_y_pos))
                yut.help = True

    yut.screen.blit(yut.background[0], (0,0))
    yut.screen.blit(yut.startButton, (yut.startButton_x_pos, yut.startButton_y_pos))
    yut.screen.blit(yut.helpButton, (yut.helpButton_x_pos, yut.helpButton_y_pos))
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