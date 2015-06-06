from random import randint
import copy

from Organism import Organism
import AnimalsAll

class Animal(Organism):
    age = 0

    def move(self, world, direction, shift, params):
        if direction is 0:   # GO RIGHT
            if self.x < (20 - shift):
                if world.organism[self.x + shift][self.y] is None:
                    world.organism[self.x + shift][self.y] = self
                    world.organism[self.x][self.y] = None
                    self.x += shift
                else:
                    params[1] = self.x + shift
                    params[2] = self.y
                    params[0] = True
        elif direction is 1:  # GO DOWN
            if self.y < (20 - shift):
                if world.organism[self.x][self.y + shift] is None:
                    world.organism[self.x][self.y + shift] = self
                    world.organism[self.x][self.y] = None
                    self.y += shift
                else:
                    params[1] = self.x
                    params[2] = self.y + shift
                    params[0] = True
        elif direction is 2:  # GO LEFT
            if self.x > (shift - 1):
                if world.organism[self.x - shift][self.y] is None:
                    world.organism[self.x - shift][self.y] = self
                    world.organism[self.x][self.y] = None
                    self.x -= shift
                else:
                    params[1] = self.x - shift
                    params[2] = self.y
                    params[0] = True
        elif direction is 3:  # GO UP
            if self.y > (shift - 1):
                if world.organism[self.x][self.y - shift] is None:
                    world.organism[self.x][self.y - shift] = self
                    world.organism[self.x][self.y] = None
                    self.y -= shift
                else:
                    params[1] = self.x
                    params[2] = self.y - shift
                    params[0] = True
        else:
            pass


    def action(self, world):
        """an Animal do something(typically moving, avoiding enemies or stay in place"""
        direction = randint(0, 3)
        shift = 1            # moving range
        call_collision, x_obstacle, y_obstacle = False, 0, 0
        params = [call_collision, x_obstacle, y_obstacle]


        self.move(world, direction, shift, params)

        if params[0] is True:
            self.collision(world, params[1], params[2])


    def give_clone(self, x_new, y_new, name):
        """returns new child of some Animals with age=0 ant appropriate coordinates"""
        if name is 'Wolf':
            return AnimalsAll.Wolf(x_new, y_new)
        elif name is 'Sheep':
            return AnimalsAll.Sheep(x_new, y_new)
        elif name is 'Fox':
            return AnimalsAll.Fox(x_new, y_new)


    def reproduce(self, world):
        """called when two Animals of the same class meets together"""
        """they look for empty label in neighboring labels"""
        x, y = randint(-1, 1), randint(-1, 1)
        if self.x + x >= 0 and self.y + y >= 0 and self.x + x <= 19 and self.y + y <= 19 and world.organism[self.x + x][self.y + y] is None:
            world.organism[self.x + x][self.y + y] = self.give_clone(self.x + x, self.y + y, self.name)
            #update new event on raportLabel
            world.raportText.set(self.name + " born at " + "[" + str(self.x + x) + "," + str(self.y + y) + "]\n" + world.raportText.get())


    def win(self, world, x_ob, y_ob):
        """called when Animal, that makes action will find WEAKER opponent"""
        #update new event on raportLabel
        world.raportText.set(self.name + " killed " + world.organism[x_ob][y_ob].name + "\n" + world.raportText.get())

        world.organism[x_ob][y_ob] = self
        world.organism[self.x][self.y] = None
        self.x = x_ob
        self.y = y_ob

    def loose(self, world, x_ob, y_ob):
        """called when Animal, that makes action will find STRONGER opponent"""
        world.raportText.set(self.name + " killed by " + world.organism[x_ob][y_ob].name + "\n" + world.raportText.get())
        world.organism[self.x][self.y] = None

    def collide(self, world, x_obstacle, y_obstacle):
        """Decide wheter type of collision it is and call appropriate behaviour"""
        if self.name is world.organism[x_obstacle][y_obstacle].name:
            #if self.age > 1 and world.organism[x_obstacle][y_obstacle].age > 1:
            self.reproduce(world)
            #else:
        elif self.strength >= world.organism[x_obstacle][y_obstacle].strength:
            self.win(world, x_obstacle, y_obstacle)
        elif self.strength < world.organism[x_obstacle][y_obstacle].strength:
            self.loose(world, x_obstacle, y_obstacle)


    def collision(self, world, x_obstacle, y_obstacle):

        # Turtle: No one who has strength more than 5 can attack Turtle
        if self.strength < 5 and world.organism[x_obstacle][y_obstacle].name is 'Turtle':
            return

        #Antelope can avoid attack and call action once more
        if world.organism[x_obstacle][y_obstacle].name is 'Antelope':
            survive = randint(0, 1)
            if survive is 1:
                world.organism[x_obstacle][y_obstacle].action(world)
                world.raportText.set("Antelope tried to run away\n" + world.raportText.get())
            else:
                world.raportText.set("Antelope has surrender\n" + world.raportText.get())
            return


        self.collide(world, x_obstacle, y_obstacle)