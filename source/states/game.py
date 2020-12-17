from datetime import time
from .. import setup
from ..components import player, dealer, deck
from .. import constants as c
from ..state import State
from ..button import TakeButton, StandButton, NextRoundButton
import pygame
from ..audio_manager import AudioManager

class Game(State):

    def __init__(self):
        State.__init__(self)
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.player = None
        self.dealer = None
        self.deck = None
        self.stand = False
        self.dealer_stand = False
        self.show_all = False
        self.next = c.GAME_OVER_Loading
        self.font = pygame.font.SysFont(None, 30)
        self.screen = setup.SCREEN
        self.start_time = 0
        self.current_over = False

    def startup(self, current_time, persist):
        self.current_time = current_time
        self.setup_background()
        self.persist = persist
        self.setup_deck()
        self.setup_dealer()
        self.setup_player()
        self.dealer.init_card(self.deck)
        self.setup_button()

    def restart(self):
        self.player.image = setup.CharacterGFX[self.persist["player"]]
        self.deck.reset(185, 171)
        self.player.init_card(self.deck)
        self.dealer.init_card(self.deck)
        self.takeBtn.enable = True
        self.standBtn.enable = True
        self.stand = False
        self.dealer_stand = False
        self.nextRoundBtn.enable = False
        self.show_all = False

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        surface.blit(self.background, self.viewport, self.viewport)
        self.player.blitme()
        self.deck.blitme()
        self.dealer.blitme()
        self.show_card(self.show_all)
        self.check_score()
        self.dealer_take()
        self.draw_time()
        self.draw_chips_amount()
        self.check_pause(keys)

    def draw_time(self):
        self.time_msg = self.font.render(str(self.current_time), True, (255, 255, 255), (0, 0, 0))
        self.time_msg_rect = self.time_msg.get_rect()
        self.time_msg_rect.topleft = (430, 390)
        self.screen.blit(self.time_msg, self.time_msg_rect)

    def draw_chips_amount(self):
        self.player_chips_total = self.font.render(str(self.player.chips.total), True, (255, 255, 255), (0, 0, 0))
        self.player_chips_total_rect = self.player_chips_total.get_rect()
        self.player_chips_total_rect.topleft = (430, 436)
        self.screen.blit(self.player_chips_total, self.player_chips_total_rect)

    def setup_button(self):
        self.takeBtn = TakeButton(setup.SCREEN, "", 167, 409, 58, 21)
        self.standBtn = StandButton(setup.SCREEN, "", 253, 409, 58, 21)
        self.nextRoundBtn = NextRoundButton(setup.SCREEN, "", 20, 376, 93, 85)
        self.nextRoundBtn.enable = False

    def setup_background(self):
        self.background = setup.EnvGFX['Game_BG']
        self.background_rect = self.background.get_rect()

    def setup_player(self):
        self.player = player.Player(setup.SCREEN, self.persist["player"], 20, 376)
        self.player.init_card(self.deck)
        self.player.take_ante(50)

    def setup_deck(self):
        self.deck = deck.Deck(setup.SCREEN, 185, 171)

    def setup_dealer(self):
        self.dealer = dealer.Dealer(setup.SCREEN, 194, 22)

    def show_card(self, show_all: bool):
        if show_all:
            self.dealer.hands.cards[0].flip(True)
            self.dealer.hands.show(85, 55)
            self.player.hands.show(85, 230)
        else:
            self.dealer.hands.cards[0].flip(False)
            self.dealer.hands.show(85, 55)
            self.player.hands.show(85, 230)

    def check_click(self, x, y):
        if self.takeBtn.rect.collidepoint(x, y):
            if self.takeBtn.click():
                v_card = self.deck.deal()
                self.player.hit(v_card)
        elif self.standBtn.rect.collidepoint(x, y):
            if self.standBtn.click():
                self.stand = True
                self.takeBtn.enable = False
                self.standBtn.enable = False
                if self.dealer_stand:
                    self.verdict()
        elif self.nextRoundBtn.rect.collidepoint(x, y):
            if self.nextRoundBtn.click():
                self.restart()

    def dealer_take(self):
        if not self.dealer_stand:
            if self.dealer.hands.points < 17:
                if (self.current_time % 1500) < 20:
                    v_card = self.deck.deal()
                    self.dealer.hit(v_card)
            else:
                self.dealer_stand = True
                if self.stand:
                    self.verdict()

    def check_score(self):
        if self.player.hands.points > 21:
            self.takeBtn.enable = False

    def verdict(self):
        print(self.dealer.hands.points)
        print(self.player.hands.points)
        if self.dealer.hands.points > 21 and 17 <= self.player.hands.points <= 21:
                self.player.chips.win_bet()
                print("Round Win")
                self.player.image = setup.CharacterGFX[self.persist["player"] + " - win"]
        elif self.player.hands.points > 21 and 17 <= self.dealer.hands.points <= 21:
                self.player.chips.lose_bet()
                self.player.image = setup.CharacterGFX[self.persist["player"] + " - lose"]
                print("Round Lose")
        elif self.dealer.hands.points > self.player.hands.points:
            self.player.chips.lose_bet()
            self.player.image = setup.CharacterGFX[self.persist["player"] + " - lose"]
            print("Round Lose")
        else:
            self.player.image = setup.CharacterGFX[self.persist["player"] + " - push"]
            print("Round push")
        print("Click Head To Continue！")
        if self.player.chips.total <= 0:
            AudioManager().play_Lose_Sound()
            self.next = c.GAME_Lose_Loading
            self.done = True
        elif self.player.chips.total >= 200:
            AudioManager().play_Win_Sound()
            self.next = c.GAME_OVER_Loading
            self.done = True
        self.show_all = True
        self.nextRoundBtn.enable = True

    def check_pause(self, keys):
        if keys[pygame.K_ESCAPE]:
            self.next = c.Pause
            self.done = True