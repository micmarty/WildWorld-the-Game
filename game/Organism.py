from abc import ABCMeta, abstractmethod

class Organism(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def action(self, world):
        raise NotImplemented


