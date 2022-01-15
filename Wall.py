from constants import *
from random import randint


class Wall:

    def __init__(self):
        self.placeX = SIZEX  # at what X cord is the wall places
        self.gapY = randint(50, 450 - WALLGAP)  # at what y is the gap places
        self.gapSize = WALLGAP  # what is the size of the gap

    def move_wall(self):
        self.placeX -= MOVERATE


