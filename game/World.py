from tkinter import *

from game.GUI import GUI
from game.Organism import Organism


class World:
    """Container class for all organisms.
        Here are methods for:
     -displaying all organisms in labels,
     -calling next runoff"""
    organism = [[0 for x in range(20)]for y in range(20)]
    runoff = 0

    def __init__(self):
        for y in range(20):
            for x in range(20):
                self.organism[x][y] = None
        self.organism[0][0] = Organism(0, 0)
        self.organism[0][1] = Organism(0, 1)
        self.organism[0][2] = Organism(0, 2)
        self.organism[0][3] = Organism(0, 3)
        self.organism[0][4] = Organism(0, 4)
        self.organism[0][5] = Organism(0, 5)

    def move_all(self):
        for initiative in range(7, 0, -1):
            for y in range(20):
                for x in range(20):
                    if self.organism[x][y] is not None:
                        if self.organism[x][y].was is False and self.organism[x][y].initiative is initiative:
                            self.organism[x][y].was = True
                            self.organism[x][y].action(self)
        self.draw_runoff()
        self.set_all_were(False)

    def draw_runoff(self):
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is None:
                    gui.label[x][y].configure(image=PhotoImage(file='pusty.png'))
                else:
                    gui.label[x][y].configure(image=self.organism[x][y].icon)

    def set_all_were(self, new_state):
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is not None:
                    self.organism[x][y].was = new_state

if __name__ == '__main__':
    root = Tk()
    world = World()         # create just one World representation
    gui = GUI(root, world)  # sending also reference to our world
    world.draw_runoff()
    root.mainloop()

