from random import randint
from Organism import Organism
import AnimalsAll

class Animal(Organism):
    age = 0

    def action(self, world):
        direction = randint(0, 3)
        call_collision = False
        shift = 1            # moving range
        #direction = 2
        #if self.name is 'Sheep':
            #shift = 0

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

    def reproduce(self, world):
        for i in range(-1,1,2):
            for j in range(-1,1,2):
                if self.x > 0 and self.y > 0 and self.x < (20-1) and self.y< (20-1):
                    if world.organism[self.x + i][self.y + j] is None:
                        if self.name is 'Wolf':
                            world.organism[self.x + i][self.y + j] = AnimalsAll.Wolf(self.x + i, self.y + j)
                            world.raportText.set(self.name + " born at [" + str(self.x + i) + "," + str(self.y + j) + "]" + "\n" + world.raportText.get())
                        elif self.name is 'Sheep':
                            world.organism[self.x + i][self.y + j] = AnimalsAll.Sheep(self.x + i, self.y + j)
                            world.raportText.set(self.name + " born at [" + str(self.x + i) + "," + str(self.y + j) + "]" + "\n" + world.raportText.get())

    def win(self, world, x_ob, y_ob):
        #TODO displaying in raportbox
        world.raportText.set(self.name + " killed " + world.organism[x_ob][y_ob].name + "\n" + world.raportText.get())
        world.organism[x_ob][y_ob] = self
        world.organism[self.x][self.y] = None
        self.x = x_ob
        self.y = y_ob

    def loose(self, world, x_ob, y_ob):
        #TODO displaying in raportbox
        world.organism[self.x][self.y] = None

    def collision(self, world, x_obstacle, y_obstacle):
        if self.name is world.organism[x_obstacle][y_obstacle].name:
            self.reproduce(world)
        elif self.strength >= world.organism[x_obstacle][y_obstacle].strength:
            self.win(world, x_obstacle, y_obstacle)
        elif self.strength < world.organism[x_obstacle][y_obstacle].strength:
            self.loose(world, x_obstacle, y_obstacle)