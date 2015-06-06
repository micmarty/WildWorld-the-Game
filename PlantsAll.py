from tkinter import PhotoImage
from Plant import Plant
from random import randint

class Grass(Plant):

    def __init__(self, x, y):
        self.name = 'Grass'
        self.x = x
        self.y = y

        self.strength = 0
        self.initiative = 0

        self.icon = PhotoImage(file='icons/trawa.png')

class SowThistle(Plant):

    def __init__(self, x, y):
        self.name = 'SowThistle'
        self.x = x
        self.y = y

        self.strength = 0
        self.initiative = 0

        self.icon = PhotoImage(file='icons/mlecz.png')

    def action(self, world):
        """SowThistle has 3 attempts to spread around"""
        attempt = 3
        self.try_to_spread(world, attempt)

class Guarana(Plant):

    def __init__(self, x, y):
        self.name = 'Guarana'
        self.x = x
        self.y = y

        self.strength = 0
        self.initiative = 0

        self.icon = PhotoImage(file='icons/guarana.png')

class DeadlyNightshade(Plant):

    def __init__(self, x, y):
        self.name = 'DeadlyNightshade'
        self.x = x
        self.y = y

        self.strength = 99
        self.initiative = 0

        self.icon = PhotoImage(file='icons/wilczajagoda.png')