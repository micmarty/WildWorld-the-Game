from tkinter import PhotoImage
from game.Animal import Animal

class Sheep(Animal):

    def __init__(self, x, y):
        self.name = 'Sheep'
        self.x = x
        self.y = y

        self.strength = 4
        self.initiative = 4

        self.icon = PhotoImage(file='icons/owca.png')
        self.was = False

