from abc import abstractmethod


class State(object):

    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.next = None
        self.persist = {}

    @abstractmethod
    def startup(self, current_time, persist):
        '''abstract method'''

    def cleanup(self):
        self.done = False
        return self.persist

    @abstractmethod
    def update(self, surface, keys, current_time):
        '''abstract method'''

    @abstractmethod
    def check_click(self, x, y):
        '''abstract method'''
