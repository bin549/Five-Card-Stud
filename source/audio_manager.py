import pygame
from . import setup


class AudioManager(object):

    def __init__(self):
        self.select_theme = pygame.mixer.music.load(setup.Musics["SELECT"])

    def play_MenuTheme(self):
        pygame.mixer.music.load(setup.Musics["SELECT"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    def play_ChooseTheme(self):
        pygame.mixer.music.load(setup.Musics["梦幻伊匐园"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    def play_Player01Theme(self):
        pygame.mixer.music.load(setup.Musics["Time Passes"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    def play_Player02Theme(self):
        pygame.mixer.music.load(setup.Musics["Lullaby Set"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    def play_Win_Sound(self):
        pygame.mixer.music.load(setup.Musics["勝利"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    def play_Lose_Sound(self):
        pygame.mixer.music.load(setup.Musics["Forgotten"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

    def play_ByeBye_Sound(self):
        pygame.mixer.music.load(setup.Musics["byebye"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)


    def play_Retry_Sound(self):
        pygame.mixer.music.load(setup.Musics["Home"])
        pygame.mixer.music.play(-1, 0.0)
        pygame.mixer.music.set_volume(0.2)

# @staticmethod
    # def play_Menu():
    #     game_over_sound = pygame.mixer.Sound('resources/Sounds/game_music.ogg')
    #     game_over_sound.play()
        # pygame.mixer.music.play(-1, 0.0)
        # pygame.mixer.music.set_volume(0.2)

