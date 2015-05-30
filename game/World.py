from tkinter import *

class World:



    def __init__(self, master):

#-------MAIN WINDOW
        self.master = master
        master.title("Michal Martyniak")
        master.resizable(0, 0)


#-------FRAMES (Division main window by 2)
        lFrame = Frame(master, bg='black', width=600, height=600)
        lFrame.grid_propagate(False)

        pFrame = Frame(master, bg='white', width=500, height=500)
        pFrame.grid_propagate(False)

        lFrame.pack(side=LEFT)
        pFrame.pack(side=LEFT,fill='both')


#-------2D array of labels initalizing (each label is representing their owner)
        label = [[0 for x in range(20)] for y in range(20)]

        icon = PhotoImage(file='pusty.png')
        for y in range(20):
            for x in range(20):
                label[x][y] = Label(lFrame,image=icon,borderwidth=0)
                label[x][y].image = icon
                label[x][y].bind("<Button-1>")
                label[x][y].grid(row=y, column=x)

        img= PhotoImage(file='wolf.png')
        label[4][5].configure(image = img)
        label[4][5].image=img



root = Tk()
my_gui = World(root)
root.mainloop()
