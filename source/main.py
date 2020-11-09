import pygame
from .card import Card
from .deck import Deck
from .hands import Hands
from .person import Person
from .settings import Settings
from . import game_functions as gf
from .game_stats import GameStats


def run_game():
    pygame.init()
    settings = Settings()
    pygame.display.set_caption("Five Card Stud")
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    bg_color = (230, 230, 230)
    person = Person(settings, screen)
    gf.create_fleet(screen, screen, person)

    stats = GameStats(settings)
    stats2 = GameStats(settings)

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
