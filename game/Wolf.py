from tkinter import PhotoImage
from game.Animal import Animal

class Wolf(Animal):
    initiative = 7
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initiative = 7

        self.icon = PhotoImage(file='wolf.png')
        self.was = False
