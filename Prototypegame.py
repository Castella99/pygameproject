import pygame

class Prototype :
    screen_width = 1080 # 스크린 가로
    screen_height = 720 # 스크린 세로
    frame = 60 # 프레임
    running = True
    # 게임 시계 설정
    clock = pygame.time.Clock()
    character = None
    point = 0
    game_font = None
    start_ticks = 0 # 시작 tick을 받아옴
    background = None
    screen = None

    def __init__(self) :
        pygame.init() # pygame 초기화
        self.game_font = pygame.font.Font(None, 40)
        # 스크린 설정
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # 게임 폰트 설정
        self.game_font = pygame.font.Font(None, 40)
        
        self.start_ticks = pygame.time.get_ticks() # 시작 tick을 받아옴
        # 이벤트 루프 구현 (메서드 오버라이딩)

    
   

        
        