from Neuron import Neuron


class Brain:

    def __init__(self):  # (value, weight)
        self.inputs = []
        self.lvl1 = []
        self.output = 0
        for i in range(4):
            self.inputs.append(Neuron())
            self.lvl1.append(Neuron())

    def calculate(self):
        # calculating lvl 1
        for n in self.lvl1:
            n.value = 1
            for i in self.inputs:
                n.value += i.value * i.weight

        #  calculate output
        self.output = 1
        for n in self.lvl1:
            self.output += n.value * n.weight

        self.output = int(self.output + 0.5)

    def mutate(self, num):
        for n in self.inputs:
            n.weight += num * n.weight
        for n in self.lvl1:
            n.weight += num * n.weight



