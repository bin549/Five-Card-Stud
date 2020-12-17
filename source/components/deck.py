import random
from .card import Card
from pygame.sprite import Sprite
from .. import setup

suits = ["spade", "heart", "diamond", "club"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck(Sprite):

    def __init__(self, screen, x, y):
        super(Deck, self).__init__()
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank, screen))
        self.shuffle()
        self.screen = screen
        self.setup_image(x, y)
        self.choose_image()

    def shuffle(self):
        random.shuffle(self.cards)

    def setup_image(self, x, y):
        self.image1 = setup.CardGFX['deck1']
        self.image2 = setup.CardGFX['deck2']
        self.image1_rect = self.image1.get_rect()
        self.image2_rect = self.image2.get_rect()
        self.image1_rect.topleft = (x, y)
        self.image2_rect.topleft = (x, y)

    def choose_image(self):
        image_index = random.randint(0, 1)
        if image_index:
            self.image = self.image1
            self.rect = self.image1_rect
        else:
            self.image = self.image2
            self.rect = self.image2_rect

    def deal(self):
        self.choose_image()
        return self.cards.pop()

    def reset(self, x, y):
        self.__init__(self.screen, x, y)

    def __str__(self):
        return " ".join([card.__str__() for card in self.cards]) + "\n"

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blit_handcards(self):
        for card in self.cards:
            print(card.image_name)
            card.set_pos(random.randint(0, self.screen.get_rect()[2]),
                         random.randint(0, self.screen.get_rect()[3]))
            card.blitme()