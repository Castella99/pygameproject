import os
import pygame

class Player : # 플레이어 객체
    x_pos = 0 # 객체의 x좌표
    y_pos = 0 # 객체의 y좌표
    pos = (x_pos, y_pos) # 객체의 좌표 튜플
    path = os.path.dirname(os.path.abspath(__file__)) # 경로 받아오기
    meeple = ["blue.png", "green.png", "purple.png", "red.png", "sky.png", "yellow.png"] # 말의 파일명 리스트

    def __init__(self, mee) : # 정수로 meeple의 idx 받이오기
        pygame.image.load(self.path+"/meeple/"+self.meeple[mee]) # 해당 말의 이미지 가져오기

    