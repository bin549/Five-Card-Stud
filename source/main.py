from . import tools
from .states import menu, loading, game
from . import constants as c
from . import button
import pygame


GAME_VERSION = 'V1.0'
REC_SIZE = 50
CHESS_RADIUS = REC_SIZE//2 - 2
CHESS_LEN = 15
MAP_WIDTH = CHESS_LEN * REC_SIZE
MAP_HEIGHT = CHESS_LEN * REC_SIZE

INFO_WIDTH = 200
BUTTON_WIDTH = 140
BUTTON_HEIGHT = 50
 
SCREEN_WIDTH = MAP_WIDTH + INFO_WIDTH
SCREEN_HEIGHT = MAP_HEIGHT


def run_game():
    game_loader = tools.Control()
    state_dict = {c.MENU: menu.Menu(),
                  c.LOADING: loading.Loading(),
                  c.Game: game.Game(),
                  c.GAME_OVER: loading.GameOver(),
                  c.Retry: loading.Retry()}
    game_loader.setup_states(state_dict, c.MENU)
    game_loader.main()

    # buttons = []
    # screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    # btn1 = button.StartButton(screen, 'Get', MAP_WIDTH + 30, 15)
    # btn2 = button.GiveupButton(screen, 'Stop', MAP_WIDTH + 30, BUTTON_HEIGHT + 45)
    # buttons.append(btn1)
    # buttons.append(btn2)
    # while True:
    #     clock = pygame.time.Clock()
    #     clock.tick(60)
    #
    #     light_white = (40, 40, 40)
    #     light_black = (0, 0, 0)
    #     pygame.draw.rect(screen, light_white, pygame.Rect(
    #         0, 0, MAP_WIDTH, SCREEN_HEIGHT))
    #     pygame.draw.rect(screen, light_black, pygame.Rect(
    #         MAP_WIDTH, 0, INFO_WIDTH, SCREEN_HEIGHT))
    #     for bu in buttons:
    #         bu.draw()
    #
    #     pygame.display.update()
    """background, gameover, settings, screen = gf.init_game()
    blackjack = Blackjack(settings, screen)
    blackjack.loop_run()"""
