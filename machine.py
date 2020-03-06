import random as rn
from time import sleep


class Neuron:
    def __init__(self):
        self.__Importance = 0
        self.neuron_made()

    def neuron_made(self):
        self.__Importance = rn.random()

    def neuron_accuracy(self):
        pass


class NeuralNetwork:
    def __init__(self):
        self.Neuron_List = []

        while len(self.Neuron_List) <= 10:
            sleep(1)
            self.Neuron_List.append(Neuron())

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
