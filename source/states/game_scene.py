from .. import setup, tools
import pygame as pg
from .. import constants as c
from ..components import person


class GameScene(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.person = None

    def startup(self, current_time, persist):
        self.setup_background()
        self.setup_player()
        self.setup_dealer()
        self.setup_stand()
        self.setup_deck()

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
        self.person = person.Person(self.game_info[c.PLAYER_NAME])
        self.player.rect.x = self.viewport.x + self.player_x
        self.player.rect.bottom = self.player_y
        self.viewport.x = self.player.rect.x - 110


    def setup_deck(self):
        pass

    def setup_dealer(self):
        pass

    def setup_stand(self):
        pass


"""
        background, gameover, settings, screen = gf.init_game()

        class Blackjack:

            def __init__(self):
                self.deck = Deck()
                self.dealer = Person(settings, screen)
                self.player = Person(settings, screen)
                self.stand = False
                self.over = False

            def show_some(self):
                print("Dealer's hands: ")
                self.dealer.hands.cards[0].face_up = False
                print(self.dealer.hands)
                print("Player's hands: ")
                print(self.player.hands)

            def show_all(self):
                print("Dealer's hands: ")
                self.dealer.hands.cards[0].face_up = True
                print(self.dealer.hands)
                print("Player's hands: ")
                print(self.player.hands)

            def start(self):
                self.deck.reset()
                self.stand = False
                self.dealer.init_card(self.deck)
                self.player.init_card(self.deck)
                self.show_some()

            def player_hit(self):
                while not self.stand:
                    x = input("Player stand or hit, Enter s or h: ")
                    if x[0] == 'h':
                        self.player.hit(self.deck.deal())
                    elif x[0] == 's':
                        self.stand = True
                    self.show_some()
                    if self.player.hands.points > 21:
                        print("Player bunst, Dealer wins")
                        self.player.chips.lose_bet()
                        self.stand = True

            def run(self):
                self.start()
                self.player_hit()
                while self.dealer.hands.points < 17:
                    self.dealer.hit(self.deck.deal())
                self.show_all()
                if self.dealer.hands.points > 21 or self.dealer.hands.points < self.player.hands.points:
                    print("Player wins")
                    self.player.chips.win_bet()
                elif self.dealer.hands.points > self.player.hands.points:
                    print("Dealer wins")
                    self.player.chips.lose_bet()
                    if self.player.chips.total <= 0:
                        print("no money boy need go home.")
                        self.over = True
                else:
                    print("It's a push")d

                print("player stand at :" + str(self.player.chips.total))

            def loop_run(self):
                print("welcome to my Blackjack world!")
                x = int(input("Please take your ante: "))
                self.player.take_ante(x)
                while True:
                    self.run()
                    if self.over:
                        break
                    else:
                        x = input("Once again? Enter y or n: ")
                        if x[0] == 'y':
                            continue
                        else:
                            break
"""
