
from .. import setup
from .. import tools
from .. import constants as c
import pygame as pg
from .. components import info


class GameOver(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        persist = {}
        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        self.next = c.Game_LOADING
       # self.persist = persist
        #self.game_info = persist
        #self.overhead_info = info.Info(self.game_info, c.MAIN_MENU)
        self.setup_background()
        self.setup_player()
        # self.setup_cursor()

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        # self.game_info[c.CURRENT_TIME] = self.current_time
        # self.player_image = self.player_list[self.player_index][0]
        # self.player_rect = self.player_list[self.player_index][1]
        self.update_cursor(keys)
        # self.overhead_info.update(self.game_info)
        #
        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.player, self.viewport, self.viewport)
        # surface.blit(self.image_dict['GAME_NAME_BOX'][0],
        #              self.image_dict['GAME_NAME_BOX'][1])
        # surface.blit(self.player_image, self.player_rect)
        # surface.blit(self.cursor.image, self.cursor.rect)
        # self.overhead_info.draw(surface)

    def setup_player(self):
        self.player = setup.CardGFX['black_joker']
        self.player_rect = self.player.get_rect()
        self.player = pg.transform.scale(self.player,
                                         (int(self.player_rect.width * c.BACKGROUND_MULTIPLER),
                                          int(self.player_rect.height * c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

        # self.player_list = []
        # player_rect_info = [(178, 32, 12, 16), (178, 128, 12, 16)]
        # for rect in player_rect_info:
        #     image = tools.get_image(setup.CardGFX['black_joker'], *rect, c.BLACK, 2.9)
        #     rect = image.get_rect()
        #     rect.x, rect.bottom = 110, c.GROUND_HEIGHT
        #     self.player_list.append((image, rect))
        # self.player_index = 0

    def setup_background(self):
        self.background = setup.EnvGFX['BackGround']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                              int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        # self.image_dict = {}
        # image = tools.get_image(setup.GFX['title_screen'], 1, 60, 176, 88,
        #                         (255, 0, 220), c.SIZE_MULTIPLIER)
        # rect = image.get_rect()
        # rect.x, rect.y = (170, 100)
        # self.image_dict['GAME_NAME_BOX'] = (image, rect)

    def setup_cursor(self):
        # self.cursor = pg.sprite.Sprite()
        # self.cursor.image = tools.get_image(
        #     setup.GFX[c.ITEM_SHEET], 24, 160, 8, 8, c.BLACK, 3)
        # rect = self.cursor.image.get_rect()
        # rect.x, rect.y = (220, 358)
        # self.cursor.rect = rect
        # self.cursor.state = c.PLAYER1
        pass

    def update_cursor(self, keys):
        # if self.cursor.state == c.PLAYER1:
        #     self.cursor.rect.y = 358
        #     if keys[pg.K_DOWN]:
        #         self.cursor.state = c.PLAYER2
        #         self.player_index = 1
        #         self.game_info[c.PLAYER_NAME] = c.PLAYER_MONKEY
        # elif self.cursor.state == c.PLAYER2:
        #     self.cursor.rect.y = 403
        #     if keys[pg.K_UP]:
        #         self.cursor.state = c.PLAYER1
        #         self.player_index = 0
        if keys[pg.K_RETURN]:
            self.done = True

