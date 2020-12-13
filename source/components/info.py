import pygame as pg
from .. import constants as c
from .. import setup, tools


class Character(pg.sprite.Sprite):

    def __init__(self, image):
        pg.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()


class Info(object):

    def __init__(self, game_info, state):
        self.game_info = game_info
        self.state = state
        self.create_font_image_dict()
        self.create_state_labels()

    def create_font_image_dict(self):
        self.image_dict = {}
        image_list = []

        image_rect_list = [  # 0 - 9
            (3, 230, 7, 7), (12, 230, 7, 7), (19, 230, 7, 7),
            (27, 230, 7, 7), (35, 230, 7, 7), (43, 230, 7, 7),
            (51, 230, 7, 7), (59, 230, 7, 7), (67, 230, 7, 7),
            (75, 230, 7, 7),
            # A - Z
            (83, 230, 7, 7), (91, 230, 7, 7), (99, 230, 7, 7),
            (107, 230, 7, 7), (115, 230, 7, 7), (123, 230, 7, 7),
            (3, 238, 7, 7), (11, 238, 7, 7), (20, 238, 7, 7),
            (27, 238, 7, 7), (35, 238, 7, 7), (44, 238, 7, 7),
            (51, 238, 7, 7), (59, 238, 7, 7), (67, 238, 7, 7),
            (75, 238, 7, 7), (83, 238, 7, 7), (91, 238, 7, 7),
            (99, 238, 7, 7), (108, 238, 7, 7), (115, 238, 7, 7),
            (123, 238, 7, 7), (3, 246, 7, 7), (11, 246, 7, 7),
            (20, 246, 7, 7), (27, 246, 7, 7), (48, 246, 7, 7),
            # -*
            (68, 249, 6, 2), (75, 247, 6, 6)]

        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        for character, image_rect in zip(character_string, image_rect_list):
            self.image_dict[character] = tools.get_image(setup.CardGFX['text_images'],
                                                         *image_rect, (92, 148, 252), 2.9)

    def create_state_labels(self):
        if self.state == c.MENU:
            self.create_main_menu_labels()

    def create_main_menu_labels(self):
        mario_game = []
        luigi_game = []

        self.create_label(mario_game, c.PLAYER1, 272, 360)
        self.create_label(luigi_game, c.PLAYER2, 272, 405)
        self.state_labels = [mario_game, luigi_game]

    def create_label(self, label_list, string, x, y):
        for letter in string:
            label_list.append(Character(self.image_dict[letter]))
        self.set_label_rects(label_list, x, y)

    def set_label_rects(self, label_list, x, y):
        for i, letter in enumerate(label_list):
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            letter.rect.y = y
            if letter.image == self.image_dict['-']:
                letter.rect.y += 7
                letter.rect.x += 2

    def update(self, level_info, level=None):
        self.level = level
        self.handle_level_state(level_info)

    def handle_level_state(self, level_info):
        pass

    def draw(self, surface):
        self.draw_info(surface, self.state_labels)

    def draw_info(self, surface, label_list):
        for label in label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)