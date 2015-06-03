from tkinter import PhotoImage
from game.Animal import Animal

class Wolf(Animal):
    initiative = 7
    def __init__(self, x, y):
        #TODO add 'name'
        self.x = x
        self.y = y
        self.initiative = 7

        self.icon = PhotoImage(file='icons/wolf.png')
        self.was = False
