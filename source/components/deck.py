import random
from .card import Card
from pygame.sprite import Sprite
from .. import setup

suits = ["spade", "heart", "diamond", "club"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck(Sprite):

    def __init__(self, screen):
        super(Deck, self).__init__()
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank, screen))
        self.shuffle()

        self.screen = screen
        self.image = setup.CGFX['deck']
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.screen = screen

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def reset(self):
        self.__init__()

    def __str__(self):
        return " ".join([card.__str__() for card in self.cards]) + "\n"

    def blitme(self):
        self.screen.blit(self.image, self.rect)