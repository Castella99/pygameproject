import os
import pygame


class Background:
    path = os.path.dirname(os.path.abspath(__file__))
    screen_width = 1080  # 스크린 가로
    screen_height = 720  # 스크린 세로
    prompt = "start"
    background_images = [
        pygame.image.load(path + "/background/empty.png"),
        pygame.image.load(path + "/background/start.png"),
        pygame.image.load(path + "/background/table color reverse.png"),
        pygame.image.load(path + "/background/help.PNG"),
        pygame.image.load(path + "/background/finish.png"),
        pygame.image.load(path + "/background/board.png"),
        pygame.image.load(path + "/background/setting.png")
    ]
    background_dict = {"empty": 0, "start": 1, "table": 2,
                       "help": 3, "finish": 4, "board": 5, "setting":6}

    def __init__(self, prompt):
        self.image = self.background_images[self.background_dict[prompt]]

    def put_image(self, prompt):  # 배경 객체의 prompt로 이미지를 변경함.
        self.image = self.background_images[self.background_dict[prompt]]
        return self.image
