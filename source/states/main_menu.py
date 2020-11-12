from .. import tools
from .. import setup


class Menu(tools.State):

    def __init__(self):
        tools.State.__init__(self)

    def startup(self, current_time, persist):
        self.setup_background()
        self.setup_cursor()

    def setup_background(self):
        self.background = setup.GFX['level_1']
        self.background_rect = self.background.get_rect()
        self.background = pg.transform.scale(self.background,
                                             (int(self.background_rect.width * c.BACKGROUND_MULTIPLER),
                                              int(self.background_rect.height * c.BACKGROUND_MULTIPLER)))

        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        self.image_dict = {}
        image = tools.get_image(setup.GFX['title_screen'], 1, 60, 176, 88,
                                (255, 0, 220), c.SIZE_MULTIPLIER)
        rect = image.get_rect()
        rect.x, rect.y = (170, 100)
        self.image_dict['GAME_NAME_BOX'] = (image, rect)

    def setup_cursor(self):
        self.cursor = pg.sprite.Sprite()
        self.cursor.image = tools.get_image(setup.GFX[c.ITEM_SHEET], 24, 160, 8, 8, c.BLACK, 3)
        rect = self.cursor.image.get_rect()
        rect.x, rect.y = (220, 358)
        self.cursor.rect = rect
        self.cursor.state = c.PLAYER1

    def update(self, surface, keys, current_time):
