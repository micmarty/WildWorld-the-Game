from game.Organism import Organism
from random import randint
import game.Wolf


class Animal(Organism):
    age = 0

    def action(self, world):
        direction = randint(0, 4)
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
            world.organism[self.x][self.y].collision(world, x_obstacle, y_obstacle)

    def collision(self, world, x_obstacle, y_obstacle):
        #TODO make something reasonable
        world.organism[x_obstacle+1][y_obstacle] = game.Wolf.Wolf(x_obstacle + 1, y_obstacle)