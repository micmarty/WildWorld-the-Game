from random import randint
import copy

from Organism import Organism
import PlantsAll

class Plant(Organism):
    age = 0

    def spread(self, world, x_new, y_new):
        """Plant copy itself"""
        if self.name is 'Grass':
            world.organism[x_new][y_new] = PlantsAll.Grass(x_new, y_new)
        elif self.name is 'SowThistle':
            world.organism[x_new][y_new] = PlantsAll.SowThistle(x_new, y_new)
        elif self.name is 'Guarana':
            world.organism[x_new][y_new] = PlantsAll.Guarana(x_new, y_new)
        elif self.name is 'DeadlyNightshade':
            world.organism[x_new][y_new] = PlantsAll.DeadlyNightshade(x_new, y_new)

    def try_to_spread(self, world, attempt):
        """Plants look for empty space for growing"""

        for attempts in range(attempt):  # Plant can make multiple attempts for spreading around
            direction = randint(0, 9)

            if direction is 0:    # RIGHT
                if self.x < 19 and world.organism[self.x + 1][self.y] is None:
                    self.spread(world, self.x + 1, self.y)
            elif direction is 1:  # DOWN
                if self.y > 0 and world.organism[self.x][self.y - 1] is None:
                    self.spread(world, self.x, self.y - 1)
            elif direction is 1:  # DOWN
                if self.x > 0 and world.organism[self.x - 1][self.y] is None:
                    self.spread(world, self.x - 1, self.y)
            elif direction is 1:  # UP
                if self.y < 19 and world.organism[self.x][self.y + 1] is None:
                    self.spread(world, self.x, self.y + 1)
            else:
                pass

    def action(self, world):
        """a Plant do something(typically spreads,but stays in place"""
        attempt = 1
        self.try_to_spread(world, attempt)

    def collision(self, world, x_obstacle, y_obstacle):
        """Plants doesn't move. They won't collide"""
        pass