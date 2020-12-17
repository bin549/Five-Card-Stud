from .. import setup
from .. import constants as c
from ..state import State
from ..components import deck
import pygame
from ..audio_manager import AudioManager

class GameLose(State):

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
        self.setup_deck()

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.blit(self.background, self.viewport, self.viewport)
        self.rasc()
        self.check_pause(keys)

    def setup_deck(self):
        self.deck = deck.Deck(setup.SCREEN, 185, 171)

    def setup_background(self):
        self.background = setup.EnvGFX['LoserBG']
        self.background_rect = self.background.get_rect()

    def rasc(self):
        self.deck.blit_handcards()


    def check_pause(self, keys):
        if keys[pygame.K_ESCAPE]:
            self.next = c.Pause
            self.done = True