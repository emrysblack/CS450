from sklearn import datasets
import random


def compute_accuracy(predict, key):
    positives = 0
    for index in range(len(predict)):
        if int(predict[index]) is int(key[index]):
            positives += 1
    return positives / len(predict)


class HardCoded:
    def train(self, data, target):
        return False

    def predict(self, data):
        results = []
        for item in data:
            results.append(0)
        return results

iris = datasets.load_iris()

# Show the data (the attributes of each instance)
print(iris.data)

# Show the target values (in numeric format) of each instance
print(iris.target)

# Show the actual target names that correspond to each number
print(iris.target_names)

# randomize the instances using same random order for data and targets
seed = random.random()
random.seed(seed)
random.shuffle(iris.data)
random.shuffle(iris.target)

# split into lists of 70% and 30%
training_num = int(len(iris.data)*.7)
training_set = iris.data[:training_num]
training_set_targets = iris.target[:training_num]
testing_set = iris.data[training_num:]
testing_set_targets = iris.target[training_num:]

# create instance of classifier
hard_coded = HardCoded

hard_coded.train(hard_coded,training_set, training_set_targets)
testing_set_results = hard_coded.predict(hard_coded,testing_set)


print(iris.data[training_num:])

# Show the target values (in numeric format) of each instance
print(iris.target[training_num:])

# Show the actual target names that correspond to each number
print(iris.target_names)

# show accuracy results as percent
print(str(int(compute_accuracy(testing_set_results, iris.target[training_num:]) * 100)) + "%")