from .. import setup, tools
import pygame as pg
# from ..components import person
from ..components import player, dealer, deck, card
# import time
from .. import button
from .. import constants as c


class Game(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.buttons = []
        self.player = None
        self.dealer = None
        self.deck = None
        # self.screen = pg.display.set_mode(
        #     (c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        #
        # self.stand = False
        self.next = c.GAME_OVER_Loading

    def startup(self, current_time, persist):
        print("welcome to my Blackjack world!")
        self.setup_background()
        self.setup_player()
        self.setup_dealer()
        self.setup_deck()
        self.setup_button()
        # self.start()
        self.draw_button()
        self.player.blitme()
        self.deck.blitme()
        self.dealer.blitme()
        # title
        # score

    def update(self, surface, keys, current_time):
        self.update_cursor(keys)

    def setup_button(self):
        btn1 = button.StartButton(setup.SCREEN, 'Get',  30, 15)
        btn2 = button.GiveupButton(setup.SCREEN, 'Stop',  30, 45)
        self.buttons.append(btn1)
        self.buttons.append(btn2)

    def draw_button(self):
        light_white = (40, 40, 40)
        light_black = (0, 0, 0)
        pg.draw.rect(setup.SCREEN, light_white, pg.Rect(0, 0, c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        pg.draw.rect(setup.SCREEN, light_black, pg.Rect(c.SCREEN_WIDTH, 0, c.SCREEN_HEIGHT, c.SCREEN_HEIGHT))
        for btn in self.buttons:
            btn.draw()

    def setup_background(self):
        self.background = setup.CardGFX['b1fh']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.background_rect.width * c.BACKGROUND_MULTIPLER),
                                              int(self.background_rect.height * c.BACKGROUND_MULTIPLER)))
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    def setup_player(self):
        self.player = player.Player(setup.SCREEN)

    def setup_deck(self):
        self.deck = deck.Deck(setup.SCREEN)

    def setup_dealer(self):
        self.dealer = dealer.Dealer(setup.SCREEN)

    def update_cursor(self, keys):
        if keys[pg.K_ESCAPE]:
            self.done = True

    # def show_some(self):
    #     print("Dealer's hands: ")
    #     self.dealer.hands.cards[0].flip(False)
    #     print(self.dealer.hands)
    #     self.dealer.hands.draw_us()
    #     print("Player's hands: ")
    #     print(self.player.hands)
    #     self.player.hands.draw_us()
    #
    # def show_all(self):
    #     print("Dealer's hands: ")
    #     self.dealer.hands.cards[0].flip(True)
    #     print(self.dealer.hands)
    #     self.dealer.hands.draw_us()
    #     print("Player's hands: ")
    #     print(self.player.hands)
    #     self.player.hands.draw_us()
    #
    # def start(self):
    #     self.deck.reset()
    #     self.stand = False
    #     self.dealer.init_card(self.deck)
    #     self.player.init_card(self.deck)
    #     self.show_some()
    #     x = int(input("Please take your ante: "))
    #     self.player.take_ante(x)
    #     # while not self.done:
    #    #     self.run()
    #
    # def player_hit(self):
    #     while not self.stand:
    #         x = input("Player stand or hit, Enter s or h: ")
    #         if x[0] == 'h':
    #             v_card = self.deck.deal()
    #             v_card.blitme()
    #             self.player.hit(v_card)
    #         elif x[0] == 's':
    #             self.stand = True
    #         if self.player.hands.points > 21:
    #             print("Player bunst, Dealer wins")
    #             self.player.chips.lose_bet()
    #             self.stand = True
    #
    # def run(self):
    #     self.player_hit()
    #     while self.dealer.hands.points < 17:
    #         v_card = self.deck.deal()
    #         v_card.blitme()
    #         self.dealer.hit(v_card)
    #         time.sleep(100)
    #     self.show_all()
    #     if self.dealer.hands.points > 21 or self.dealer.hands.points < self.player.hands.points:
    #         print("Player wins")
    #         self.player.chips.win_bet()
    #     elif self.dealer.hands.points > self.player.hands.points:
    #         print("Dealer wins")
    #         self.player.chips.lose_bet()
    #     else:
    #         print("It's a push")
    #
    #     if self.player.chips.total <= 0:
    #         print("no money boy need go home.")
    #         self.next = c.GAME_OVER
    #         self.done = True
    #
    #     print("player stand at :" + str(self.player.chips.total))

