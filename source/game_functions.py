import sys
import pygame
from .settings import Settings


def init_game():
    pygame.init()

    pygame.display.set_caption("Five Card Stud")

    pygame.mixer.music.load('resources/Sounds/植松伸夫 - Shuffle or Boogie.mp3')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.2)

    background = pygame.image.load('resources/Sprites/Character/Monkey.png')
    gameover = pygame.image.load('resources/Sprites/Character/Monkey.png')

    game_over_sound = pygame.mixer.Sound('resources/Sounds/game_music.ogg')
    game_over_sound.set_volume(0.3)

    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))

    return background, gameover, settings, screen


def update_screen(settings, screen, player):
    screen.fill(settings.bg_color)
    player.blitme()
    pygame.display.flip()


def create_fleet(settings, screen, player):
    pass


def check_events(settings, screen, player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, player)


def check_keydown_events(event, settings, screen, player):
    if event.key == pygame.K_RIGHT:
        sound = pygame.mixer.Sound('resource/Sounds/Effect/bullet.wav')
