from random import uniform


class Neuron:
    def __init__(self):
        self.value = 0
        self.weight = uniform(-1, 1)
