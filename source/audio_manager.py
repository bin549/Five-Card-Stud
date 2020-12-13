import sys
import pygame


class AudioManager(object):

    @staticmethod
    def play():
        menu_music: str = 'resources/Sounds/Music/Prelude.mp3'
        pygame.mixer.music.load(menu_music)
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    # game_over_sound = pygame.mixer.Sound('resources/Sounds/game_music.ogg')
    # game_over_sound.set_volume(0.3)
