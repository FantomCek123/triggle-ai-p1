import pygame

pygame.font.init()

SCREEN_WIDTH = None
SCREEN_HEIGHT= None
WIN_WIDTH = None
WIN_HEIGHT = None
BG = None
WIN = None
PLAY_TEXT = None
OPTION_TEXT = None
QUIT_TEXT = None
BACK_FONT = None
RESOLUTION_FONT = None
RESOLUTION_NUMBER_FONT = None
PLAY_TEXT_BIG = None
OPTION_TEXT_BIG = None
QUIT_TEXT_BIG = None
BACK_FONT_BIG = None
RESOLUTION_FONT_BIG = None
RESOLUTION_NUMBER_FONT_BIG = None
CLOCK_RATE = 60

def set_settings():
    global BG, PLAY_TEXT, OPTION_TEXT, QUIT_TEXT, BACK_FONT, RESOLUTION_FONT, RESOLUTION_NUMBER_FONT, WIN
    global PLAY_TEXT_BIG, OPTION_TEXT_BIG, QUIT_TEXT_BIG, BACK_FONT_BIG, RESOLUTION_FONT_BIG, RESOLUTION_NUMBER_FONT_BIG
    global WIN_WIDTH, WIN_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

    WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    if WIN_HEIGHT is None or WIN_WIDTH is None:
        screen_info = pygame.display.Info()
        SCREEN_WIDTH = screen_info.current_w
        SCREEN_HEIGHT = screen_info.current_h
        WIN_WIDTH = SCREEN_WIDTH
        WIN_HEIGHT = SCREEN_HEIGHT

    BG = pygame.transform.scale(pygame.image.load('assets/images/TrinityForce_background.jpg'),
                                (SCREEN_WIDTH,SCREEN_HEIGHT))

    PLAY_TEXT = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 12))
    OPTION_TEXT = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 30))
    QUIT_TEXT = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 30))
    BACK_FONT = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 17.143))
    RESOLUTION_FONT = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 17.143))
    RESOLUTION_NUMBER_FONT = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 20))

    PLAY_TEXT_BIG = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 10))
    OPTION_TEXT_BIG = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 20))
    QUIT_TEXT_BIG = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 20))
    BACK_FONT_BIG = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 13.333))
    RESOLUTION_FONT_BIG = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 13.333))
    RESOLUTION_NUMBER_FONT_BIG = pygame.font.SysFont("Super Caramel", int(WIN_HEIGHT / 17.143))



    pygame.display.set_caption('TrinityForce')

def set_resolution(res):
    global WIN_HEIGHT,WIN_WIDTH
    WIN_WIDTH, WIN_HEIGHT = res
    set_settings()

def horizontal_resolution_offset():
    global SCREEN_WIDTH,WIN_WIDTH
    return (SCREEN_WIDTH - WIN_WIDTH) / 2

def vertical_resolution_offset():
    global SCREEN_HEIGHT,WIN_HEIGHT
    return (SCREEN_HEIGHT - WIN_HEIGHT) / 2

