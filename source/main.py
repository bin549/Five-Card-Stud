from . import tools
from .states import menu, loading, game, character_select, game_over
from . import constants as c


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
