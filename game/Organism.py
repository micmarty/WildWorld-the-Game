from tkinter import PhotoImage


class Organism:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.initiative = 7

        self.icon = PhotoImage(file='wolf.png')
        self.was = False

    def action(self,world):
        world.organism[self.x + 1][self.y] = self
        world.organism[self.x][self.y] = None
        self.x += 1

