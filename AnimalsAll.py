from tkinter import PhotoImage
from Animal import Animal
from random import randint

class Wolf(Animal):

    def __init__(self, x, y):
        self.name = 'Wolf'
        self.x = x
        self.y = y

        self.strength = 9
        self.initiative = 5

        self.icon = PhotoImage(file='icons/wolf.png')

class Sheep(Animal):

    def __init__(self, x, y):
        self.name = 'Sheep'
        self.x = x
        self.y = y

        self.strength = 4
        self.initiative = 4

        self.icon = PhotoImage(file='icons/owca.png')

class Fox(Animal):

    def __init__(self, x, y):
        self.name = 'Fox'
        self.x = x
        self.y = y

        self.strength = 3
        self.initiative = 7

        self.icon = PhotoImage(file='icons/lis.png')

    def action(self, world):
        """Fox doesn't move on label, where opponent is stronger that himself"""

        direction = randint(0, 3)   # random direction
        shift = 1                   # moving range

        # Collision FLAG, opponent's <x> and <y>
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]

        self.move(world, direction, shift, params)

        if params[0] is True:

            # ADDED FOX's power - > avoiding stronger enemies
            if self.name is 'Fox' and world.organism[params[1]][params[2]].strength > self.strength:
                world.raportText.set("Fox avoided danger situation\n" + world.raportText.get())
                return

            self.collision(world, params[1], params[2])

class Turtle(Animal):

    def __init__(self, x, y):
        self.name = 'Turtle'
        self.x = x
        self.y = y

        self.strength = 2
        self.initiative = 1

        self.icon = PhotoImage(file='icons/zolw.png')

    def action(self, world):
        """Turtle moves seldom, it has lower chance to take a step"""

        direction = randint(0, 15)  # random direction
        shift = 1                   # moving range

        #collision FLAG, opponent's coordinates
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]

        self.move(world, direction, shift, params)

        if params[0] is True:
            self.collision(world, params[1], params[2])

class Antelope(Animal):

    def __init__(self, x, y):
        self.name = 'Antelope'
        self.x = x
        self.y = y

        self.strength = 4
        self.initiative = 4

        self.icon = PhotoImage(file='icons/antylopa.png')

    def action(self, world):
        """Antelope makes two steps at once"""
        direction = randint(0, 3)   # random direction
        shift = 2                   # Antelope has wider range

        #collision FLAG, opponent's coordinates
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]

        self.move(world, direction, shift, params)

        if params[0] is True:
            self.collision(world, params[1], params[2])

class Human(Animal):

    def __init__(self, x, y):
        self.name = 'Human'
        self.x = x
        self.y = y

        self.strength = 5
        self.initiative = 4

        self.icon = PhotoImage(file='icons/czlowiek.png')

        self.elixir_works = False
        self.drinking_round = 0

    def action(self, world):
        """Human goes wherever you want, keys: W S A D"""

        direction = world.h_dir     # variable hidden in World class
        shift = 1                   # moving range

        #collision FLAG, opponent's coordinates
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]

        if direction is 'elixir':   # when 't' key pressed, power is enabled
            if self.elixir_works is False:
                self.drinking_round = world.runoff + 5  # elixir works through 5 rounds
                self.elixir_works = True
                self.strength = 10                      # starting strength

                # updating infoLabel
                world.infoText.set("Elixir used. It will stop working in round "+ str(self.drinking_round)+"\n"+world.infoText.get())
            else:

                #updating infoLabel
                world.infoText.set("Elixir already works\n" + world.infoText.get())
        else:   # standard movement handling
            self.move(world, direction, shift, params)

        # There is necessity to check if elixir should stop working
        if self.elixir_works is True:
            if self.strength > 5:
                self.strength -= 1  # every round human strength is smaller

                #updating infoLabel
                world.infoText.set("Current human strength: " + str(self.strength) + "\n" + world.infoText.get())
            else:
                # turning FLAG off, after 5 rounds
                self.elixir_works = False

        if params[0] is True:
            self.collision(world, params[1], params[2])

