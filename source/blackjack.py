from person import Person
from deck import Deck


class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.dealer = Person()
        self.player = Person()
        self.stand = False

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
        x = int(input("Please take your ante: "))
        self.player.take_ante(x)

        self.dealer.init_card(deck)
        self.player.init_card(deck)

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
        print("welcome to my Blackjack world!")

        self.start()

        self.player_hit()

        while self.dealer.hands.points < 17:
            self.dealer.hit(deck.deal())

        self.show_all()

        if self.dealer.hands.points > 21 or self.dealer.hands.points < self.player.hands.points:
            print("Player wins")
            self.player.chips.win_bet()
        elif self.dealer.hands.points > self.player.hands.points:
            print("Dealer wins")
            self.player.chips.lose_bet()
        else:
            print("It's a push")

        print("player stand at :" + str(blackjack.player.chips.total))

    def loop_run(self):
        while True:
            self.run()
            x = input("Once again? Enter y or n: ")
            if x[0] == 'y':
                continue
            else:
                break
