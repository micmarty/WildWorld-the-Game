from abc import ABCMeta, abstractmethod

class Organism(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def action(self, world):
        """Moving around - animals
        Spreading around - plants"""
        raise NotImplemented

    @abstractmethod
    def collision(self, world, x_obstacle, y_obstacle):
        """Killing, reproducing...of Organisms"""
        raise NotImplemented


