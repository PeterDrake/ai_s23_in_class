import math
import random


class InputNeuron:

    def __init__(self, activation):
        self.activation = activation


class Neuron:

    def __init__(self, previous_layer):
        self.activation = None
        self.previous_layer = previous_layer
        # Later we'll need a delta value
        self.weights = [random.gauss(0, 1) for _ in previous_layer]

    def __repr__(self):
        return str([f'{self.previous_layer[i]} -> {self.weights[i]}' for i in range(len(self.previous_layer))])

    def update_activation(self):
        s = sum(self.weights[i] * self.previous_layer[i].activation for i in range(len(self.previous_layer)))
        self.activation = logistic(s)


def logistic(x):
    """
    Logistic sigmoid squashing function.
    """
    return 1 / (1 + math.exp(-x))


n = Neuron([InputNeuron(0.2), InputNeuron(0.7)])

print(n)
print(n.activation)
n.update_activation()
print(n.activation)
