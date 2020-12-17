from pygame.sprite import Sprite
from .. import setup

rank_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
suit_codes = {"spade": "\u2660", "heart": "\u2661",
              "diamond": "\u2663", "club": "\u2662"}
suit_values = {"spade": 4, "heart": 3, "diamond": 1, "club": 2}


class Card(Sprite):

    def __init__(self, suit, rank, screen):
        super(Card, self).__init__()
        self.suit = suit
        self.rank = rank
        self.point = rank_points[rank]
        self.face_up = True
        self.strength = rank_values[rank] * 10 + suit_values[suit]

        self.image_name = self.suit + "_" + self.rank
        self.screen = screen
        self.image = setup.CardGFX[self.image_name]
        self.hide_image = setup.CardGFX["back"]
        self.rect = self.image.get_rect()

    def set_pos(self, x, y):
        self.rect.topleft = (x, y)

    def __str__(self):
        if not self.face_up:
            return "<hole card>"
        return suit_codes[self.suit] + self.rank

    def __gt__(self, other):
        return self.strength > other.strength

    def __eq__(self, other):
        return self.strength == other.strength

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return self.strength < other.strength

    def __le__(self, other):
        return self < other or self == other

    def flip(self, dir_up):
        if dir_up:
            self.face_up = True
        else:
            self.face_up = False

    def blitme(self):
        if self.face_up:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.hide_image, self.rect)

