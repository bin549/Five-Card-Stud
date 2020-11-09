import sys
import pygame

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