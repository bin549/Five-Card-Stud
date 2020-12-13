from .hands import Hands
from .chips import Chips
from .. import setup
from .person import Person

class Dealer(Person):

    def __init__(self, screen):
        super(Dealer, self).__init__(screen)
        self.screen = screen
        self.image = setup.CharacterGFX['alien']

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.hands = Hands()
        self.chips = Chips()

    def init_card(self, deck, num=2):
        self.hands.reset_card()
        for _ in range(num):
            self.hands.add_card(deck.deal())

    def take_ante(self, ante):
        self.chips.ante = ante

    def hit(self, card):
        self.hands.add_card(card)

    def blitme(self):
        self.screen.blit(self.image, self.rect)