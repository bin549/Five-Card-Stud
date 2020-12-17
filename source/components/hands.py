
class Hands:

    def __init__(self):
        self.cards = []
        self.points = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.points += card.point

        if card.rank == 'A':
            self.aces += 1

        while self.points > 21 and self.aces:
            self.points -= 10
            self.aces -= 1

    def reset_card(self):
        Hands.__init__(self)

    def __str__(self):
        return " ".join([card.__str__() for card in self.cards]) + "\n"

    def __getitem__(self, pos):
        return self.cards[pos]

    def show(self, x, y):
        for index, card in enumerate(self.cards):
            card.set_pos(x + 80 * index, y)
            card.blitme()
