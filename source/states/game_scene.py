from .. import setup, tools
import pygame as pg
from .. import constants as c
from ..components import person
from ..components import player
from ..components import dealer
from ..components import deck
from ..components import card
import time


class GameScene(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.player = None
        self.dealer = None
        self.deck = None
        self.screen = pg.display.set_mode(
            (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

        self.stand = False
        self.next = c.LOAD_SCREEN

    def startup(self, current_time, persist):
        print("welcome to my Blackjack world!")
        self.setup_background()
        self.setup_player()
        self.setup_dealer()
        self.setup_deck()

        self.start()

        self.player.blitme()
        self.dealer.blitme()
        self.deck.blitme()

        self.run()

    def update(self, surface, keys, current_time):
        surface.blit(self.background, self.viewport, self.viewport)

    def setup_background(self):
        self.background = setup.CGFX['b1fh']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.background_rect.width * c.BACKGROUND_MULTIPLER),
                                              int(self.background_rect.height * c.BACKGROUND_MULTIPLER)))
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    def setup_player(self):
        self.player = player.Player(self.screen)

    def setup_deck(self):
        self.deck = deck.Deck(self.screen)

    def setup_dealer(self):
        self.dealer = dealer.Dealer(self.screen)

    def show_some(self):
        print("Dealer's hands: ")
        self.dealer.hands.cards[0].flip(False)
        print(self.dealer.hands)
        self.dealer.hands.draw_us()
        print("Player's hands: ")
        print(self.player.hands)
        self.player.hands.draw_us()

    def show_all(self):
        print("Dealer's hands: ")
        self.dealer.hands.cards[0].flip(True)
        print(self.dealer.hands)
        self.dealer.hands.draw_us()
        print("Player's hands: ")
        print(self.player.hands)
        self.player.hands.draw_us()

    def start(self):
        self.deck.reset()
        self.stand = False
        self.dealer.init_card(self.deck)
        self.player.init_card(self.deck)
        self.show_some()
        x = int(input("Please take your ante: "))
        self.player.take_ante(x)
        #while not self.done:
       #     self.run()

    def player_hit(self):
        while not self.stand:
            x = input("Player stand or hit, Enter s or h: ")
            if x[0] == 'h':
                v_card = self.deck.deal()
                v_card.blitme()
                self.player.hit(v_card)
            elif x[0] == 's':
                self.stand = True
            if self.player.hands.points > 21:
                print("Player bunst, Dealer wins")
                self.player.chips.lose_bet()
                self.stand = True

    def run(self):
        self.player_hit()
        while self.dealer.hands.points < 17:
            v_card = self.deck.deal()
            v_card.blitme()
            self.dealer.hit(v_card)
            time.sleep(100)
        self.show_all()
        if self.dealer.hands.points > 21 or self.dealer.hands.points < self.player.hands.points:
            print("Player wins")
            self.player.chips.win_bet()
        elif self.dealer.hands.points > self.player.hands.points:
            print("Dealer wins")
            self.player.chips.lose_bet()
        else:
            print("It's a push")

        if self.player.chips.total <= 0:
            print("no money boy need go home.")
            self.next = c.GAME_OVER
            self.done = True

        print("player stand at :" + str(self.player.chips.total))
