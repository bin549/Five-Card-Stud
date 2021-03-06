from random import random
from .. import setup
from .. import constants as c
from ..state import State
from ..components import deck
from ..button import MenuButton, RetryButton
from ..audio_manager import AudioManager


class GameOver(State):

    def __init__(self):
        State.__init__(self)
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        persist = {}
        self.startup(0.0, persist)
        self.deck = None

    def startup(self, current_time, persist):
        self.persist = persist
        self.next = c.Game_LOADING
        self.setup_background()
        self.setup_button()

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.blit(self.background, self.viewport, self.viewport)

    def setup_background(self):
        self.background = setup.EnvGFX['GO_BG']
        self.background_rect = self.background.get_rect()

    def setup_button(self):
        self.menuBtn = MenuButton(setup.SCREEN, "", 66, 262, 148, 37)
        self.retryBtn = RetryButton(setup.SCREEN, "", 66, 335, 148, 37)

    def check_click(self, x, y):
        if self.menuBtn.rect.collidepoint(x, y):
            if self.menuBtn.click():
                self.next = c.MENU
                AudioManager().play_MenuTheme()
                self.done = True
        elif self.retryBtn.rect.collidepoint(x, y):
                self.next = c.Game
                AudioManager().play_Retry_Sound()
                self.done = True
