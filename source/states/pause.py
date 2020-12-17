from .. import setup
from .. import constants as c
from ..state import State
from ..button import MenuButton, RetryButton
from ..audio_manager import AudioManager
AudioManager().play_MenuTheme()

class Pause(State):

    def __init__(self):
        State.__init__(self)
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    def startup(self, current_time, persist):
        self.persist = persist
        self.next = c.Game_LOADING
        self.setup_background()
        self.setup_button()

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.blit(self.background, self.viewport, self.viewport)

    def setup_background(self):
        self.background = setup.EnvGFX['Pause']
        self.background_rect = self.background.get_rect()

    def setup_button(self):
        self.menuBtn = MenuButton(setup.SCREEN, "", 177, 238, 148, 37)
        self.retryBtn = RetryButton(setup.SCREEN, "", 177, 311, 148, 37)

    def check_click(self, x, y):
        if self.menuBtn.rect.collidepoint(x, y):
            if self.menuBtn.click():
                self.next = c.MENU
                self.done = True
                AudioManager().play_MenuTheme()
        elif self.retryBtn.rect.collidepoint(x, y):
                self.next = c.Game
                self.done = True
