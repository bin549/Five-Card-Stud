from .. import setup, tools


class GameScene(tools.State):

    def __init__(self):
        tools.State.__init__(self)
        self.player = None


