from constants import *
from Brain import Brain


class Bird:

    def __init__(self):
        self.placeY = SIZEY/2  # place for bird in the screen
        self.speed = 0   # where id the bird going to move (up or down and how much)
        self.brain = Brain()
        self.score = 0

    def move_bird(self):
        self.placeY += self.speed
        self.speed += GRAVITY

    def jump(self):
        self.speed = JUMP

    def cpy(self, bird):
            self.brain = bird.brain