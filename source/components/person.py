from .hands import Hands
from .chips import Chips
from pygame.sprite import Sprite
from .. import setup


class Person(Sprite):

    def __init__(self, screen):
        super(Person, self).__init__()
        self.screen = screen
        self.image = setup.GFX['Cute']
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
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

