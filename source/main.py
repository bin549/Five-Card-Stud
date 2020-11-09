import pygame
from .card import Card
from .deck import Deck
from .hands import Hands
from .person import Person
from . import game_functions as gf
from .game_stats import GameStats

BACKGROUND_IMAGE_HEIGHT = 800


def run_game():
    background, gameover, settings, screen = gf.init_game()

    bg_color = (230, 230, 230)
    person = Person(settings, screen)
    gf.create_fleet(settings, screen, person)
    stats = GameStats(settings)

    """
    card1 = Card("spade", 'A')
    card2 = Card("heart", 'A')
    print(card1 > card2)
    c = [card1, card2]
    print(max(c))
    print(card1.strength)
    print(card2.strength)

    card1 = Card("spade", 'A')
    card2 = Card("heart", 'A')
    card3 = Card("spade", 'K')

    hands = Hands()
    hands.add_card(card1)
    hands.add_card(card2)
    hands.add_card(card3)
    print(hands.cards[1])
    """

    person = Person()
    deck = Deck()
    person.init_card(deck)
    print(person.hands)

    while True:
        gf.check_events(settings, screen, person)

        if stats.game_active:
            person.update()
        gf.update_screen(settings, screen, person)
