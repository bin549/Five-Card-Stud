import pygame
from pygame.locals import *

BUTTON_WIDTH = 140
BUTTON_HEIGHT = 50


class Button(object):

    def __init__(self, screen, text, x, y, color, enable):
        self.screen = screen
        self.width = BUTTON_WIDTH
        self.height = BUTTON_HEIGHT
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.enable = enable
        self.font = pygame.font.SysFont(None, BUTTON_HEIGHT*2//3)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = (x, y)
        self.text = text
        self.init_msg()

    def init_msg(self):
        if self.enable:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
        else:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        if self.enable:
            self.screen.fill(self.button_color[0], self.rect)
        else:
            self.screen.fill(self.button_color[1], self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class StartButton(Button):

    def __init__(self, screen, text, x, y):
        super().__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)

    def click(self, game):
        pass
        # if self.enable:
        #     game.start()
        #     game.winner = None
        #     self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
        #     self.enable = False
        #     return True
        # return False

    def unclick(self):
        pass
        # if not self.enable:
        #     self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
        #     self.enable = True


class GiveupButton(Button):

    def __init__(self, screen, text, x, y):
        super().__init__(screen, text, x, y, [(230, 67, 64), (236, 139, 137)], False)

    def click(self, game):
        # if self.enable:
        #     game.is_play = False
        #     if game.winner is None:
        #         game.winner = game.map.reverseTurn(game.player)
        #     self.msg_image = self.font.render(
        #         self.text, True, self.text_color, self.button_color[1])
        #     self.enable = False
        #     return True
        # return False
        pass

    def unclick(self):
        # if not self.enable:
        #     self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
        #     self.enable = True
        pass
