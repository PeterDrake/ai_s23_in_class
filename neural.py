import math
import random


LEARNING_RATE = 0.1


class InputNeuron:

    def __init__(self, activation=1):
        self.activation = activation


class Neuron:

    def __init__(self, previous_layer):
        self.activation = None
        self.previous_layer = [InputNeuron()] + previous_layer  # Add bias node
        # Later we'll need a delta value
        self.weights = [random.gauss(0, 1) for _ in self.previous_layer]

    def __repr__(self):
        return str([f'{self.previous_layer[i]} -> {self.weights[i]}' for i in range(len(self.previous_layer))])

    def update_activation(self):
        s = sum(self.weights[i] * self.previous_layer[i].activation for i in range(len(self.previous_layer)))
        self.activation = logistic(s)

    def predict(self, inputs):
        inputs = [1] + inputs
        for i in range(1, len(inputs)):
            self.previous_layer[i].activation = inputs[i]
        self.update_activation()
        return self.activation

    def train(self, inputs, target):
        a = self.predict(inputs)
        t = target
        delta = -a * (1 - a) * (t - a)
        for j in range(len(self.previous_layer)):
            self.weights[j] += -LEARNING_RATE * self.previous_layer[j].activation * delta


class Network:

    def __init__(self, sizes):
        """
        :param sizes: A list of the number of neurons in each layer, e.g., [2, 2, 1] for a network that can learn XOR.
        """
        self.layers = [None] * len(sizes)
        self.layers[0] = [InputNeuron() for _ in range(sizes[0])]
        for i in range(1, len(sizes)):
            self.layers[i] = [Neuron(self.layers[i-1]) for _ in range(sizes[i])]


def logistic(x):
    """
    Logistic sigmoid squashing function.
    """
    return 1 / (1 + math.exp(-x))


# n = Neuron([InputNeuron(0), InputNeuron(0)])
# # n.weights = [-30, 20, 20]
#
# inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
# targets = [0, 1, 1, 0]
#
# for i in inputs:
#     print(n.predict(i))
#
# for _ in range(10000):
#     for i, t in zip(inputs, targets):
#         n.train(i, t)
#
# print()
# for i in inputs:
#     print(n.predict(i))

net = Network([2, 2, 1])
