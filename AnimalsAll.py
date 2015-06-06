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
        direction = randint(0, 3)
        shift = 1            # moving range
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]

        self.move(world, direction, shift, params)

        if params[0] is True:
            """ADDED FOX's power - > avoiding stronger enemies"""
            if self.name is 'Fox' and world.organism[params[1]][params[2]].strength > self.strength:
                world.raportText.set("Fox avoided danger situation\n" + world.raportText.get())
                return
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
        """Human goes wherever you want, keys: WSAD"""

        direction = world.h_dir
        shift = 1            # moving range
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]

        if direction is 'elixir':
            if self.elixir_works is False:
                self.drinking_round = world.runoff + 5
                self.elixir_works = True
                self.strength = 11
                world.infoText.set("Elixir used. It will stop working in round "+ str(self.drinking_round)+"\n"+world.infoText.get())
            else:
                world.infoText.set("Elixir already works\n" + world.infoText.get())
        else:
            self.move(world, direction, shift, params)



        if self.elixir_works is True:
            if self.strength >= 5:
                self.strength -= 1
                world.infoText.set("Current human strength: "+ str(self.strength) +"\n" + world.infoText.get())
            elif self.drinking_round is world.runoff:
                self.elixir_works = False

        if params[0] is True:
            self.collision(world, params[1], params[2])

