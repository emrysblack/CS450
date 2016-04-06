from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from math import pow, sqrt
from numbers import Number
import sys
import random


def compute_accuracy(predict, key):
    positives = 0
    answers = []
    keys = []
    # convert both to lists so we can handle any iterable input
    for item in predict:
        answers.append(item)
    for item in key:
        keys.append(item)

    for index in range(len(answers)):
        if answers[index] == keys[index]:
            positives += 1
    return positives / len(answers)


class DNode:
    def __init__(self, value):
        self.leftChild = -1
        self.rightChild = -1
        self.value = value

    def setLeft(self, index):
        self.leftChild = index

    def setRight(self, index):
        self.rightChild = index

    def getLeft(self):
        return self.leftChild

    def getRight(self):
        return self.rightChild


class DTree:
    def __init__(self, training_data):
        self.nodes = []
        self.train(training_data)

    def train(self, training_data):
        # build tree from training data
        my_data = []

    def insert(self, value):
        self.nodes.append(DNode(value))


