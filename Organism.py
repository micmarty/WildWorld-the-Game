from abc import ABCMeta, abstractmethod

class Organism(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        """To override"""
        self.name = 'Organism'
        self.x = 0
        self.y = 0

        self.strength = 0
        self.initiative = 0

        self.icon = None
        self.was = False

    @abstractmethod
    def action(self, world):
        """Moving around - animals
        Spreading around - plants"""
        raise NotImplemented

    @abstractmethod
    def collision(self, world, x_obstacle, y_obstacle):
        """Killing, reproducing...of Organisms"""
        raise NotImplemented


