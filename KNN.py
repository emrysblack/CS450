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

class HardCoded:
    def __init__(self):
        self.data = []
        self.target = []

    def train(self, train_data, train_target):
        for item in train_data:
            self.data.append(item)
        for item in train_target:
            self.target.append(item)

    def predict(self, predict_data):
        results = []
        for item in predict_data:
            results.append(self.target[0])
        return results


class NearestX:
    def __init__(self):
        self.data = []
        self.target = []

    def difference(self, left, right):
        # use subtraction for numbers and inequality for everything else
        if not isinstance(left, Number) or not isinstance(right, Number):
            if left == right:
                return 0
            else:
                return 1

        return left - right

    def train(self, train_data, train_target):
        self.data = train_data
        self.target = train_target

    def predict(self, predict_data):
        results = []
        for item in predict_data:
            # find nearest targets and take max occurrence
            nearest = self.find_nearest(item, 3)
            results.append(max(set(nearest), key=nearest.count))
        return results

    def find_nearest(self, item, num_neighbors):
        # compute item distance from other items
        position = 0
        positions = []
        for entry in self.data:
            for i in range(0, len(item)):
                position += pow(self.difference(item[i],entry[i]), 2)
            position = sqrt(position)
            positions.append(position)

        # join positions and targets and sort by shortest distances
        dist_list = list(zip(positions, self.target))
        dist_list = sorted(dist_list, key=lambda x: x[0])
        dist_list_data, dist_list_target = zip(*dist_list)

        return dist_list_target[:num_neighbors]

iris = datasets.load_iris()

# randomize the instances using same random order for data and targets

iris_list = list(zip(iris.data, iris.target))

random.shuffle(iris_list)

iris_data, iris_target = zip(*iris_list)

# split into lists of 70% and 30%
training_num = int(len(iris_data)*.7)
training_set = iris_data[:training_num]
training_set_targets = iris_target[:training_num]
testing_set = iris_data[training_num:]
testing_set_targets = iris_target[training_num:]

# create instance of hardcoded classifier
hard_coded = HardCoded()

hard_coded.train(training_set, training_set_targets)
testing_set_results = hard_coded.predict(testing_set)

# use library version to compare to your solution
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(training_set, training_set_targets)
predictions = classifier.predict(testing_set)

# create instance of my classifier
nearest_x = NearestX()

nearest_x.train(training_set, training_set_targets)
nearest_x_results = nearest_x.predict(testing_set)

# show accuracy results as percent
print("Iris Hard Coded: " + str(int(compute_accuracy(testing_set_results, iris_target[training_num:]) * 100)) + "%")

print("Iris Python KNN: " + str(int(compute_accuracy(predictions, iris_target[training_num:]) * 100)) + "%")

print("Iris My KNN: " + str(int(compute_accuracy(nearest_x_results, iris_target[training_num:]) * 100)) + "%")

if len(sys.argv) > 1:
    data, target = load_data_set(str(sys.argv[1]))
    # split into lists of 70% and 30%
    training_num = int(len(iris_data)*.7)
    training_set = data[:training_num]
    training_set_targets = target[:training_num]
    testing_set = data[training_num:]
    testing_set_targets = target[training_num:]

    # create instance of hardcoded classifier
    hard_coded = HardCoded()

    hard_coded.train(training_set, training_set_targets)
    testing_set_results = hard_coded.predict(testing_set)

    # use library version to compare to your solution
    #classifier = KNeighborsClassifier(n_neighbors=3)
    #classifier.fit(training_set, training_set_targets)
    #predictions = classifier.predict(testing_set)

    # create instance of my classifier
    nearest_x = NearestX()

    nearest_x.train(training_set, training_set_targets)
    nearest_x_results = nearest_x.predict(testing_set)

    # show accuracy results as percent
    print("Car Hard Coded: " + str(int(compute_accuracy(testing_set_results, target[training_num:]) * 100)) + "%")

    #print("Car Python KNN: " + str(int(compute_accuracy(predictions, iris_target[training_num:]) * 100)) + "%")

    print("Car My KNN: " + str(int(compute_accuracy(nearest_x_results, target[training_num:]) * 100)) + "%")