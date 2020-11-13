from . import tools
from .states import main_menu, load_screen, game_scene
from . import constants as c


def run_game():
    game = tools.Control()
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.Game_Scene: game_scene.GameScene(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.Retry: load_screen.Retry()}
    game.setup_states(state_dict, c.MAIN_MENU)
    game.main()

    """background, gameover, settings, screen = gf.init_game()
    blackjack = Blackjack(settings, screen)
    blackjack.loop_run()"""
