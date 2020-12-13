import pygame
from . import setup


class AudioManager(object):

    @staticmethod
    def play():
        pygame.mixer.music.load(setup.Musics["Prelude"])
       # pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    # game_over_sound = pygame.mixer.Sound('resources/Sounds/game_music.ogg')
    # game_over_sound.set_volume(0.3)
