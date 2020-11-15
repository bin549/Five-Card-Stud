from pygame.sprite import Sprite

class Chips(Sprite):

    def __init__(self, total=100, ante=0):
        self.total = total
        self.ante = ante

    def win_bet(self):
        self.total += self.ante

    def lose_bet(self):
        self.total -= self.ante
