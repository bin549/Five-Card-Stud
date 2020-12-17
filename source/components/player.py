from random import random
from .hands import Hands
from .chips import Chips
from .. import setup
from .person import Person

class Player(Person):

    def __init__(self, screen, name, x, y):
        super(Player, self).__init__(screen)
        self.name = name
        self.screen = screen
        self.image = setup.CharacterGFX[self.name]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
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
