from tkinter import *

from GUI import GUI
from AnimalsAll import Wolf, Sheep, Fox, Human


class World:
    """Container class for all organisms.
        Here are methods for:"""
    organism = [[0 for x in range(20)]for y in range(20)]
    h_dir = -1
    runoff = 1

    def __init__(self):
        # TEXT LABELS FOR SHOWING MOST IMPORTANT INFO
        self.raportText = StringVar()
        self.infoText = StringVar()

        #human direction variable
        self.h_dir = -1
        for y in range(20):
            for x in range(20):
                self.organism[x][y] = None
        self.organism[11][11] = Fox(11, 11)
        #self.organism[9][10] = Fox(9, 10)
        self.organism[10][10] = Human(10, 10)


    def sort(self, array):
        """sorting organisms by initiative, then by age"""
        for y in range(20):
            for x in range(20):
                if self.organism[x][y] is not None:
                    array.append(world.organism[x][y])
        array[:] = sorted(array, key=lambda Organism: (Organism.initiative, Organism.age), reverse=True)


    def move_all(self):
        """call action for all organisms and drawing later. Increases runoff number, ang """
        self.infoText.set("ROUND : " + str(self.runoff) + "\n")
        sorted_organisms = []
        self.sort(sorted_organisms)

        for i in sorted_organisms:
            if self.organism[i.x][i.y] is i:
                i.action(self)
                i.age += 1
        self.draw_runoff()
        self.runoff += 1



    def draw_runoff(self):
        """display appropriate icons in labels, if there's no organism->show empty png file"""
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

