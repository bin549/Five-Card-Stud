import sys
import pygame


def initGame():
    pygame.mixer.music.load('resource/Sounds/game_music.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.2)

    background = pygame.image.load('resources/Sprites/background.png')
    gameover = pygame.image.load('resource/Sprites/gameover.png')

    game_over_sound = pygame.mixer.Sound('resource/sound/game_over.wav')
    game_over_sound.set_volume(0.3)

    return (background, gameover)


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