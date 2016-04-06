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


def load_data_set(data_file, shuffle = True):
    data_set = []
    data = []
    target = []

    f = open(data_file, 'r')
    for line in f:
        data_set.append(line)
    if shuffle:
        random.shuffle(data_set)
    # split into data and target
    for item in data_set:
        item = item[:len(item)-1] # throw away newline
        item = item.split(',')
        data.append(item[:len(item)-1])
        target.append(item[len(item)-1:])
        target_list = [val for sublist in target for val in sublist]
    return data, target_list


class DNode:
    def __init__(self, value):
        self.children = []
        self.value = value


class DTree:
    def __init__(self, training_data):
        self.nodes = []
        self.train(training_data)

    def train(self, training_data):
        # build tree from training data
        my_data = []

    def insert(self, value):
        self.nodes.append(DNode(value))
