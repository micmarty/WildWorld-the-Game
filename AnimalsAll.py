from tkinter import PhotoImage
from Animal import Animal

class Wolf(Animal):

    def __init__(self, x, y):
        self.name = 'Wolf'
        self.x = x
        self.y = y

        self.strength = 9
        self.initiative = 5

        self.icon = PhotoImage(file='icons/wolf.png')

class Sheep(Animal):

    def __init__(self, x, y):
        self.name = 'Sheep'
        self.x = x
        self.y = y

        self.strength = 4
        self.initiative = 4

        self.icon = PhotoImage(file='icons/owca.png')

class Fox(Animal):

    def __init__(self, x, y):
        self.name = 'Fox'
        self.x = x
        self.y = y

        self.strength = 3
        self.initiative = 7

        self.icon = PhotoImage(file='icons/lis.png')
