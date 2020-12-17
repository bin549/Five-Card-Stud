from .. import setup, tools
from .. import constants as c
from abc import abstractmethod, ABC
from ..state import State


class Loading(State):

    def __init__(self):
        State.__init__(self)
        self.time_list = [200, 200, 200]
        self.background = None
        self.background_rect = None
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)

    @abstractmethod
    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.next = self.set_next_state()

    @abstractmethod
    def set_next_state(self):
        pass

    @abstractmethod
    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.fill(c.BLACK)
        elif (current_time - self.start_time) < self.time_list[1]:
            surface.fill((255, 5, 5))
        elif (current_time - self.start_time) < self.time_list[2]:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class GameLoading(Loading, ABC):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [300, 320, 323]
        self.persist = {}
        self.startup(0.0, self.persist)

    def set_next_state(self):
        return c.Game

    def cleanup(self) -> dict:
        return self.persist

    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.fill(c.BLACK)
        elif (current_time - self.start_time) < self.time_list[1]:
            surface.fill((255, 5, 5))
        elif (current_time - self.start_time) < self.time_list[2]:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class CharacterSelectLoading(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [300, 600, 900]
        self.background = setup.EnvGFX['CharacterSelectLoading']
        self.background_rect = self.background.get_rect()

    def set_next_state(self):
        return c.Character_Select

    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.blit(self.background, self.viewport, self.viewport)
        elif (current_time - self.start_time) < self.time_list[1]:
            self.background = setup.EnvGFX['CharacterSelectLoading - 2']
            surface.blit(self.background, self.viewport, self.viewport)
        elif (current_time - self.start_time) < self.time_list[2]:
            self.background = setup.EnvGFX['CharacterSelectLoading - 3']
            surface.blit(self.background, self.viewport, self.viewport)
        else:
            self.done = True


class GameOverLoading(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [600]
        self.background = setup.EnvGFX['GameWin']

    def startup(self, current_time, persist):
        self.persist = persist
        self.start_time = current_time
        self.next = self.set_next_state()

    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.blit(self.background, self.viewport, self.viewport)
        else:
            self.done = True

    def set_next_state(self):
        return c.GAME_OVER


class GameLoseLoading(Loading):

    def __init__(self):
        Loading.__init__(self)
        self.time_list = [600]
        self.background = setup.EnvGFX['GameLose']

    def startup(self, current_time, persist):
        self.persist = persist
        self.start_time = current_time
        self.next = self.set_next_state()

    def update(self, surface, keys, current_time):
        if (current_time - self.start_time) < self.time_list[0]:
            surface.blit(self.background, self.viewport, self.viewport)
        else:
            self.done = True

    def set_next_state(self):
        return c.GAME_Lose
