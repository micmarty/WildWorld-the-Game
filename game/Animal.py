from game.Organism import Organism
from random import randint

class Animal(Organism):
    age = 0

    def action(self, world):
        direction = randint(0, 4)
        shift = 1            # moving range
        if direction is 0:   # GO RIGHT
            if self.x < (20 - shift):
                if world.organism[self.x + shift][self.y] is None:
                    world.organism[self.x + shift][self.y] = self
                    world.organism[self.x][self.y] = None
                    self.x += shift
                else:
                    #TODO impement what to if collision is detected, here
                    pass
        elif direction is 1:  # GO DOWN
            if self.y < (20 - shift):
                if world.organism[self.x][self.y + shift] is None:
                    world.organism[self.x][self.y + shift] = self
                    world.organism[self.x][self.y] = None
                    self.y += shift
                else:
                    #TODO impement what to if collision is detected, here
                    pass
        elif direction is 2:  # GO LEFT
            if self.x > (shift - 1):
                if world.organism[self.x - shift][self.y] is None:
                    world.organism[self.x - shift][self.y] = self
                    world.organism[self.x][self.y] = None
                    self.x -= shift
                else:
                    #TODO impement what to if collision is detected, here
                    pass
        elif direction is 3:  # GO UP
            if self.y > (shift - 1):
                if world.organism[self.x][self.y - shift] is None:
                    world.organism[self.x][self.y - shift] = self
                    world.organism[self.x][self.y] = None
                    self.y -= shift
                else:
                    #TODO impement what to if collision is detected, here
                    pass