from .. import setup
from ..state import State
from .. import constants as c
from ..button import StartButton, QuitButton
from ..audio_manager import AudioManager
import time

class Menu(State):

    def __init__(self):
        State.__init__(self)
        persist = {}
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        self.next = c.Character_Select_Loading
        self.setup_background()
        self.setup_button()
        AudioManager().play_MenuTheme()

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.blit(self.background, self.viewport, self.viewport)

    def check_click(self, x, y):
        if self.startBtn.rect.collidepoint(x, y):
            if self.startBtn.click():
                self.done = True
                AudioManager().play_ChooseTheme()
        elif self.QuitBtn.rect.collidepoint(x, y):
            AudioManager().play_ByeBye_Sound()
            time.sleep(4.2)
            self.QuitBtn.click()

    def setup_background(self):
        self.background = setup.EnvGFX['BG']
        self.background_rect = self.background.get_rect()

    def setup_button(self):
        self.startBtn = StartButton(setup.SCREEN, "", 194, 298)
        self.QuitBtn = QuitButton(setup.SCREEN, "", 194, 344)
