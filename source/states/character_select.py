from .. import setup
from .. import constants as c
from ..state import State
from ..button import ConfirmButton
from ..audio_manager import AudioManager

class CharacterSelect(State):

    def __init__(self):
        State.__init__(self)
        self.persist = {}
        self.startup(0.0, self.persist)
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    def startup(self, current_time, persist):
        self.next = c.Game_LOADING
        self.setup_background()
        self.persist = persist
        self.setup_player()


    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.player1, self.player1_rect)
        surface.blit(self.player2, self.player2_rect)

    def setup_player(self):
        self.player1 = setup.CharacterGFX['1']
        self.player2 = setup.CharacterGFX['2']
        self.player1_rect = self.player1.get_rect()
        self.player2_rect = self.player2.get_rect()
        self.player1_pos = (122, 204)
        self.player2_pos = (291, 203)
        self.player1_rect.topleft = self.player1_pos
        self.player2_rect.topleft = self.player2_pos
        self.player1_button = ConfirmButton(setup.SCREEN, "", self.player1_pos[0], self.player1_pos[1], self.player1_rect[2], self.player1_rect[3])
        self.player2_button = ConfirmButton(setup.SCREEN, "", self.player2_pos[0], self.player2_pos[1], self.player2_rect[2], self.player2_rect[3])

    def setup_background(self):
        self.background = setup.EnvGFX['CS_BG']
        self.background_rect = self.background.get_rect()

    def check_click(self, x, y):
        if self.player1_button.rect.collidepoint(x, y):
            if self.player1_button.click():
                self.persist["player"] = "1"
                self.done = True
                AudioManager().play_Player01Theme()
        elif self.player2_button.rect.collidepoint(x, y):
            if self.player2_button.click():
                self.persist["player"] = "2"
                self.done = True
                AudioManager().play_Player02Theme()
