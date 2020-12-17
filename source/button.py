import pygame
from abc import abstractmethod
from . import constants as c


class Button(object):

    def __init__(self, screen, text, x, y, color, enable):
        self.screen = screen
        self.width = c.BUTTON_WIDTH
        self.height = c.BUTTON_HEIGHT
        self.button_color = color
        self.text_color = (255, 255, 255)
        self.enable = enable
        self.font = pygame.font.SysFont(None, c.BUTTON_HEIGHT*2//3)
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

    @abstractmethod
    def click(self):
        pass

class StartButton(Button):

    def __init__(self, screen, text, x, y):
        super().__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)

    def click(self):
        if self.enable:
            return True
        return False


class QuitButton(Button):

    def __init__(self, screen, text, x, y):
        super().__init__(screen, text, x, y, [(230, 67, 64), (236, 139, 137)], True)

    def click(self):
        if self.enable:
            pygame.quit()
        pass


class ConfirmButton(Button):

    def __init__(self, screen, text, x, y, width, heigh):
        super().__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)
        self.width = width
        self.height = heigh
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = (x, y)

    def click(self):
        if self.enable:
            return True
        return False


class TakeButton(ConfirmButton):

    def __init__(self, screen, text, x, y, width, heigh):
        super().__init__(screen, text, x, y, width, heigh)

    def click(self):
        if self.enable:
            return True
        return False


class StandButton(ConfirmButton):

    def __init__(self, screen, text, x, y, width, heigh):
        super().__init__(screen, text, x, y, width, heigh)

    def click(self):
        if self.enable:
            return True
        return False


class NextRoundButton(ConfirmButton):

    def __init__(self, screen, text, x, y, width, heigh):
        super().__init__(screen, text, x, y, width, heigh)

    def click(self):
        if self.enable:
            return True
        return False


class MenuButton(ConfirmButton):

    def __init__(self, screen, text, x, y, width, heigh):
        super().__init__(screen, text, x, y, width, heigh)

    def click(self):
        if self.enable:
            return True
        return False


class RetryButton(ConfirmButton):

    def __init__(self, screen, text, x, y, width, heigh):
        super().__init__(screen, text, x, y, width, heigh)

    def click(self):
        if self.enable:
            return True
        return False
