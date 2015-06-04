from tkinter import PhotoImage
from game.Animal import Animal
class Wolf(Animal):

    def __init__(self, x, y):
        self.name = 'Wolf'
        self.x = x
        self.y = y

        self.strength = 9
        self.initiative = 5

        self.icon = PhotoImage(file='icons/wolf.png')
        self.was = False
