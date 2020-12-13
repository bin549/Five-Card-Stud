from .. import setup, tools
from .. import constants as c
# from ..components import info
from abc import abstractmethod


class Loading(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.time_list = [200, 200, 200]

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        # self.game_info = self.persist
        self.next = self.set_next_state()
        # info_state = self.set_info_state()
        # self.overhead_info = info.Info(self.game_info, info_state)

    @abstractmethod
    def set_next_state(self):
        pass

    @abstractmethod
    def set_info_state(self):
        return c.Game

    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.fill(c.BLACK)
        elif (current_time - self.start_time) < self.time_list[1]:
            surface.fill((255, 5, 5))
        elif (current_time - self.start_time) < self.time_list[2]:
            surface.fill((106, 150, 252))
        else:
            self.done = True
            # self.overhead_info.update(self.game_info)
            # self.overhead_info.draw(surface)


class GameLoading(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [300, 320, 323]

    def set_next_state(self):
        return c.Game

    def set_info_state(self):
        return c.GAME_OVER


class CharacterSelectLoading(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [300, 320, 325]

    def set_next_state(self):
        return c.Character_Select

    def set_info_state(self):
        return c.GAME_OVER


class GameOverLoading(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [3000, 3200, 3235]

    def set_next_state(self):
        return c.GAME_OVER

    def set_info_state(self):
        return c.GAME_OVER


class Retry(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [3000, 3200, 3235]

    def set_next_state(self):
        return c.Game
