from . import tools
from .states import menu, loading, game, character_select, game_over
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
                  c.Character_Select_Loading: loading.CharacterSelectLoading(),
                  c.Character_Select: character_select.CharacterSelect(),
                  c.Game_LOADING: loading.GameLoading(),
                  c.Game: game.Game(),
                  c.GAME_OVER_Loading: loading.GameOverLoading(),
                  c.GAME_OVER: game_over.GameOver(),
                  c.Retry: loading.Retry()}
    game_loader.setup_states(state_dict, c.MENU)
    game_loader.main()


    """background, gameover, settings, screen = gf.init_game()
    blackjack = Blackjack(settings, screen)
    blackjack.loop_run()"""
