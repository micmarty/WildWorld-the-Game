from random import randint
import copy

from Organism import Organism
import AnimalsAll

class Animal(Organism):
    age = 0

    def move(self):
        #TODO typical movement here
        pass


    def action(self, world):
        """an Animal do something(typically moving, avoiding enemies or stay in place"""
        direction = randint(0, 3)
        call_collision = False
        shift = 1            # moving range

        if direction is 0:   # GO RIGHT
            if self.x < (20 - shift):
                if world.organism[self.x + shift][self.y] is None:
                    world.organism[self.x + shift][self.y] = self
                    world.organism[self.x][self.y] = None
                    self.x += shift
                else:
                    x_obstacle = self.x + shift
                    y_obstacle = self.y
                    call_collision = True
        elif direction is 1:  # GO DOWN
            if self.y < (20 - shift):
                if world.organism[self.x][self.y + shift] is None:
                    world.organism[self.x][self.y + shift] = self
                    world.organism[self.x][self.y] = None
                    self.y += shift
                else:
                    x_obstacle = self.x
                    y_obstacle = self.y + shift
                    call_collision = True
        elif direction is 2:  # GO LEFT
            if self.x > (shift - 1):
                if world.organism[self.x - shift][self.y] is None:
                    world.organism[self.x - shift][self.y] = self
                    world.organism[self.x][self.y] = None
                    self.x -= shift
                else:
                    x_obstacle = self.x - shift
                    y_obstacle = self.y
                    call_collision = True
        elif direction is 3:  # GO UP
            if self.y > (shift - 1):
                if world.organism[self.x][self.y - shift] is None:
                    world.organism[self.x][self.y - shift] = self
                    world.organism[self.x][self.y] = None
                    self.y -= shift
                else:
                    x_obstacle = self.x
                    y_obstacle = self.y - shift
                    call_collision = True
        else:
            pass

        if call_collision is True:
            self.collision(world, x_obstacle, y_obstacle)


    def give_clone(self, x_new, y_new):
        """returns new child of some Animals with age=0 ant appropriate coordinates"""
        z = copy.deepcopy(self)
        z.x = x_new
        z.y = y_new
        z.age = 0
        return z


    def reproduce(self, world):
        """called when two Animals of the same class meets together"""
        """they look for empty label in neighboring labels"""
        x, y = randint(-1, 1), randint(-1, 1)
        if self.x + x >= 0 and self.y + y >= 0 and self.x + x <= 19 and self.y + y <= 19 and world.organism[self.x + x][self.y + y] is None:
            #update new event on raportLabel
            #TODO HUGE PROBLEM, cloning didn't work. Propably need to hardcode it :(
            world.organism[self.x + x][self.y + y] = AnimalsAll.Fox(self.x + x, self.y + y)#self.give_clone(self.x + x, self.y + y)
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

    def collision(self, world, x_obstacle, y_obstacle):
        """Decide wheter type of collision it is and call appropriate behaviour"""
        if self.name is world.organism[x_obstacle][y_obstacle].name:
            #if self.age > 1 and world.organism[x_obstacle][y_obstacle].age > 1:
            self.reproduce(world)
            #else:
        elif self.strength >= world.organism[x_obstacle][y_obstacle].strength:
            self.win(world, x_obstacle, y_obstacle)
        elif self.strength < world.organism[x_obstacle][y_obstacle].strength:
            self.loose(world, x_obstacle, y_obstacle)