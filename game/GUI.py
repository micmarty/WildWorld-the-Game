from tkinter import *

class GUI:

    def insert(self,event, n, m):
        img = PhotoImage(file='zolw.png')
        self.label[n][m].configure(image = img)
        self.label[n][m].image = img



    def __init__(self, master):

#-------MAIN WINDOW
        self.master = master
        master.title("Michal Martyniak")
        master.resizable(0, 0)

#-------FRAMES (Division main window by 2)
        self.lFrame = Frame(master, bg='black', width=600, height=600)
        self.lFrame.grid_propagate(False)

        self.pFrame = Frame(master, bg='white', width=500, height=500)
        self.pFrame.grid_propagate(False)

        self.lFrame.pack(side=LEFT)
        self.pFrame.pack(side=LEFT,fill='both')


#-------2D array of labels initalizing (each label is representing their owner)
        self.label = [[0 for x in range(20)] for y in range(20)]

        icon = PhotoImage(file='pusty.png')
        for y in range(20):
            for x in range(20):
                self.label[x][y] = Label(self.lFrame,image=icon,borderwidth=0)
                self.label[x][y].image = icon
                self.label[x][y].grid(row=y, column=x)
                #self.label[x][y].bind("<Button-1>", self.insert(x, y))
                def make_lambda(x,y):
                    return lambda ev: self.insert(ev, x, y)
                self.label[x][y].bind("<Enter>", make_lambda(x,y))


root = Tk()
my_gui = GUI(root)

root.mainloop()
