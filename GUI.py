from tkinter import *
from tkinter.filedialog import *
from random import randint
from AnimalsAll import Wolf, Sheep, Fox, Turtle, Antelope, Human
from PlantsAll import Grass, SowThistle, Guarana, DeadlyNightshade

class GUI:

    def init_frames(self):
        """sets left and right content frames"""
        self.lFrame.grid_propagate(False)

        self.pFrame = Frame(self.master, bg='white', width=500, height=500)
        self.pFrame.grid_propagate(False)

        self.lFrame.pack(side=LEFT)
        self.pFrame.pack(side=LEFT, fill='both')

    def init_labels(self, world):
        icon = PhotoImage(file='icons/pusty.png')
        for y in range(20):
            for x in range(20):
                self.label[x][y] = Label(self.lFrame, image=icon, borderwidth=0)
                self.label[x][y].image = icon
                self.label[x][y].grid(row=y, column=x)

                #Hovering at labels puts Wolf in there :D
                def make_lambda(xx, yy, worldd):
                    return lambda event: self.insertRandomly(event, xx, yy, worldd)

                def make_lambdaa(xx, yy, worldd):
                    return lambda event: self.insertFox(event, xx, yy, worldd)
                self.label[x][y].bind("<Enter>", make_lambda(x, y, world))

    def init_buttons(self, world):
        """sets three buttons: NEXT ROUND, SAVE, LOAD"""
        self.nextRun.bind("<Button-1>", lambda event: self.call_runoff(event, world))
        self.master.bind("<Return>", lambda event: self.call_runoff(event, world))
        self.master.bind("<KeyPress>", lambda e: self.key_press(e, world))
        self.nextRun.pack(side=TOP)

        self.saveButton.bind("<Button-1>", lambda event: self.save_game(event, world))
        self.saveButton.pack(side=BOTTOM)

        self.loadButton.bind("<Button-1>", lambda event: self.load_game(event, world))
        self.loadButton.pack(side=BOTTOM)

    def init_text_labels(self, world):
        world.raportText.set("\nHere will be placed info about\nkilling, dying etc..\n")
        self.raportLabel.pack(side=TOP, fill=X)

        world.infoText.set("\nWelcome!\nWSAD - move human (C icon)\nEnter - next round\n")
        self.infoLabel.pack(side=BOTTOM, fill=X)

        #text is automatically updating/changing when you add some text
        #TODO use it later... very useful example below
        #self.infoText.set("new kill\n" + self.infoText.get())

    def __init__(self, master, world):
        #-MAIN WINDOW
        self.master = master
        self.master.title("Michal Martyniak 155136")
        self.master.resizable(0, 0)

        #-FRAMES (Division main window by 2)
        self.lFrame = Frame(master, bg='black', width=600, height=600)
        self.init_frames()

        #-2D array of labels initializing ,each label is representing their owner (I mean some of Organism)
        self.label = [[0 for x in range(20)] for y in range(20)]
        self.init_labels(world)

        #-Buttons
        self.nextRun = Button(self.pFrame, text="Next round", bg='blue', relief=RIDGE, cursor='dotbox', font='consolas', borderwidth=10, padx=107, pady=32)
        self.saveButton = Button(self.pFrame, text="Save", bg='orange', relief=RIDGE, cursor='dotbox', font='consolas', borderwidth=10, padx=140, pady=30)
        self.loadButton = Button(self.pFrame, text="Load", bg='green', relief=RIDGE, cursor='dotbox', font='consolas', borderwidth=10, padx=140, pady=30)
        self.init_buttons(world)

        #-TEXT LABELS (info about dying, eating, killing, etc).
        """     dying , killing     """
        #self.raportText = StringVar()
        self.raportLabel = Label(self.pFrame, height=6, bg='red', anchor=NW, justify=LEFT, textvariable=world.raportText)

        """     eating guarana, drinking strength elixir      """
        #self.infoText = StringVar()
        self.infoLabel = Label(self.pFrame, height=6, bg='lightblue', anchor=NW, justify=LEFT, textvariable=world.infoText)

        self.init_text_labels(world)

    def save_game(self, event, world):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return

        text2save = ""
        for y in range(20):
            for x in range(20):
                if world.organism[x][y] is None:
                    text2save = str(text2save) + "-"
                elif world.organism[x][y].name is 'Wolf':
                    text2save = str(text2save) + "W"
                elif world.organism[x][y].name is 'Sheep':
                    text2save = str(text2save) + "O"
                elif world.organism[x][y].name is 'Fox':
                    text2save = str(text2save) + "L"
                elif world.organism[x][y].name is 'Turtle':
                    text2save = str(text2save) + "Z"
                elif world.organism[x][y].name is 'Antelope':
                    text2save = str(text2save) + "A"
                elif world.organism[x][y].name is 'Human':
                    text2save = str(text2save) + "C"
                elif world.organism[x][y].name is 'Grass':
                    text2save = str(text2save) + "T"
                elif world.organism[x][y].name is 'SowThistle':
                    text2save = str(text2save) + "M"
                elif world.organism[x][y].name is 'Guarana':
                    text2save = str(text2save) + "G"
                elif world.organism[x][y].name is 'DeadlyNightshade':
                    text2save = str(text2save) + "J"
            text2save = text2save + "\n"
        f.write(text2save)
        f.close() # `()` was missing.

    def load_game(self, event, world):
        x, y = 0, 0
        with askopenfile(mode='r', defaultextension=".txt") as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                else:
                    if c is 'W':
                        world.organism[x][y] = Wolf(x, y)
                    elif c is 'O':
                        world.organism[x][y] = Sheep(x, y)
                    elif c is 'L':
                        world.organism[x][y] = Fox(x, y)
                    elif c is 'Z':
                        world.organism[x][y] = Turtle(x, y)
                    elif c is 'A':
                        world.organism[x][y] = Antelope(x, y)
                    elif c is 'C':
                        world.organism[x][y] = Human(x, y)
                    elif c is 'T':
                        world.organism[x][y] = Grass(x, y)
                    elif c is 'M':
                        world.organism[x][y] = SowThistle(x, y)
                    elif c is 'G':
                        world.organism[x][y] = Guarana(x, y)
                    elif c is 'J':
                        world.organism[x][y] = DeadlyNightshade(x, y)
                    else:
                        world.organism[x][y] = None

                    if x is 19:
                        y += 1
                        x = 0
                    if x <= 18:
                        x += 1
                    if x is 19 and y is 19:
                        break

        world.draw_runoff()


    def insertRandomly(self, event, n, m, world):
        """insert randomly organisms onto hovered label, just for fun"""
        a = randint(0, 7)
        if a is 0:
            world.organism[n][m] = Wolf(n, m)
        elif a is 1:
            world.organism[n][m] = Sheep(n, m)
        elif a is 2:
            world.organism[n][m] = Fox(n, m)
        elif a is 3:
            world.organism[n][m] = Turtle(n, m)
        elif a is 4:
            world.organism[n][m] = Grass(n, m)
        elif a is 5:
            world.organism[n][m] = SowThistle(n, m)
        elif a is 6:
            world.organism[n][m] = Guarana(n, m)
        elif a is 7:
            world.organism[n][m] = DeadlyNightshade(n, m)

        self.label[n][m].configure(image=world.organism[n][m].icon)
        self.label[n][m].image = world.organism[n][m].icon

    def insertFox(self, event, n, m, world):
        """insert fox onto hovered label, just for fun"""
        world.organism[n][m] = Antelope(n, m)
        self.label[n][m].configure(image=world.organism[n][m].icon)
        self.label[n][m].image = world.organism[n][m].icon

    def key_press(self, e, world):
        """Handle directions for human movement"""
        if e.char is 'd':
            world.h_dir = 0
        elif e.char is 's':
            world.h_dir = 1
        elif e.char is 'a':
            world.h_dir = 2
        elif e.char is 'w':
            world.h_dir = 3
        elif e.char is 't':
            world.h_dir = 'elixir'
        else:
            world.h_dir = -10

    def call_runoff(self, event, world):
        """Called on NextRound button clicking, or pressing Enter"""
        world.move_all()



