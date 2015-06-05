from tkinter import *

from GUI import GUI
from AnimalsAll import Wolf

#from Sheep import Sheep


class World:
    """Container class for all organisms.
        Here are methods for:"""
    #TODO think about sorting objects, age, initiative. runoff variable should be finally used.....
    organism = [[0 for x in range(20)]for y in range(20)]
    runoff = 1

    def __init__(self):
        # TEXT LABELS FOR SHOWING MOST IMPORTANT INFO
        self.raportText = StringVar()
        self.infoText = StringVar()

        for y in range(20):
            for x in range(20):
                self.organism[x][y] = None
        self.organism[11][11] = Wolf(11, 11)
        self.organism[9][10] = Wolf(9, 10)
        self.organism[10][10] = Wolf(10, 10)


    def sort(self, list):
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is not None:
                    list.append(world.organism[x][y])
        list[:] = sorted(list, key=lambda Organism: (Organism.initiative, Organism.age), reverse=True)


    def move_all(self):
        self.infoText.set("ROUND:" + str(self.runoff) + "\n")
        sortedOrganisms = []
        self.sort(sortedOrganisms)

        for i in sortedOrganisms:
            if self.organism[i.x][i.y] is i:
                i.action(self)
                i.age += 1
        self.draw_runoff()
        self.runoff += 1



    def draw_runoff(self):
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is None:
                    gui.label[x][y].configure(image=PhotoImage(file='icons/pusty.png'))
                else:
                    gui.label[x][y].configure(image=self.organism[x][y].icon)


if __name__ == '__main__':
    root = Tk()
    world = World()         # create just one World representation
    gui = GUI(root, world)  # sending also reference to our world
    world.draw_runoff()
    root.mainloop()

