from abc import ABCMeta, abstractmethod

class Organism(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def action(self, world):
        """Moving around - animals
        Spreading around - plants"""
        raise NotImplemented

    @abstractmethod
    def collision(self, world):
        """Killing, reproducing...of Organisms"""
        raise NotImplemented


