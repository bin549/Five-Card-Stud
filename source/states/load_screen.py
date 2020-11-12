from .. import setup, tools


class LoadScreen(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.time_list = [2400, 2600, 2635]


class GameOver(LoadScreen):
    pass


class TimeOut(LoadScreen):
    pass
