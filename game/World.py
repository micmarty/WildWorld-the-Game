from tkinter import *

from game.GUI import GUI
from game.Wolf import Wolf
from game.Sheep import Sheep


class World:
    """Container class for all organisms.
        Here are methods for:"""
    #TODO think about sorting objects, age, initiative. runoff variable should be finally used.....
    organism = [[0 for x in range(20)]for y in range(20)]
    runoff = 0

    def __init__(self):
        for y in range(20):
            for x in range(20):
                self.organism[x][y] = None
        self.organism[10][10] = Wolf(10, 10)
        self.organism[2][0] = Sheep(2, 0)
        self.organism[1][1] = Sheep(1, 1)
        self.organism[0][1] = Sheep(0, 1)

    def move_all(self):
        #removed <for loop> iterating by initiative(slows down the program)
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is not None:
                    if self.organism[x][y].was is False:
                        self.organism[x][y].was = True
                        self.organism[x][y].action(self)
        self.draw_runoff()
        self.set_all_were(False)

    def draw_runoff(self):
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is None:
                    gui.label[x][y].configure(image=PhotoImage(file='icons/pusty.png'))
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

