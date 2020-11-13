from .. import setup, tools
from .. import constants as c
from ..components import info


class LoadScreen(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.time_list = [200, 200, 200]

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()
        info_state = self.set_info_state()
        self.overhead_info = info.Info(self.game_info, info_state)

    def set_next_state(self):
        return c.Game_Scene

    def set_info_state(self):
        return c.LOAD_SCREEN

    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.fill(c.BLACK)
        elif (current_time - self.start_time) < self.time_list[1]:
            surface.fill((255,5,5))
        elif (current_time - self.start_time) < self.time_list[2]:
            surface.fill((106, 150, 252))
        else:
            self.done = True
            #self.overhead_info.update(self.game_info)
            #self.overhead_info.draw(surface)


class GameOver(LoadScreen):

    def __init__(self):
        LoadScreen.__init__(self)
        self.time_list = [3000, 3200, 3235]

    def set_next_state(self):
        return c.MAIN_MENU

    def set_info_state(self):
        return c.GAME_OVER


class Retry(LoadScreen):

    def __init__(self):
        LoadScreen.__init__(self)
        self.time_list = [3000, 3200, 3235]

    def set_next_state(self):
        return c.Game_Scene