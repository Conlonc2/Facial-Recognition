
"""This is to open and read the faces from the A.I. Project."""
# Christopher Conlon
# CSC: 481 - Artificial Intelligence

#-Imports-#
from sklearn.neighbors import KNeighborsClassifier  # Kn-N algorithim
from sklearn.neural_network import MLPClassifier  # Artificial Neural Network
from sklearn.naive_bayes import GaussianNB  # Naive Bayes
import sklearn.metrics  # this will be used for accuracy, recall, and precision
import sklearn.preprocessing as pre  # used to normilize data
import ReadFile
import Features


#-Globals-#
categories = ['Male', 'Female']  # the classes we are extracting
trainList = []  # 240 males and 165 females (80%)
testList = []  # 60 males and 43 females (20%)

'''
 This function will be used to create our Kn-N model using sklearn library
'''


def kModel(dict, trainList, test):
    # This peice is to prepare our data to be fed into the sklearn function
    features = []
    expected = []
    for x in trainList:
        features.append(dict[x]['features'])
        expected.append(dict[x]['Class'])

    features = pre.normalize(features)  # Normilize the data for processing
    # Create our model
    model = KNeighborsClassifier(n_neighbors=3).fit(features, expected)
    pred = model.predict(test)
    conMatrix = sklearn.metrics.confusion_matrix(expected, pred)
    print("K-nearest neighbor Confusion Matrix\n", conMatrix, "\n")

    print("K-Nearest neighbors Algorithm: ")
    print(sklearn.metrics.classification_report(expected, pred,
                                                target_names=['Male', 'Female'], digits=2))
    return model


'''
This function will be used to create our ANN model using sklearn library
'''


def aModel(dict, trainList, test):
        # This peice is to prepare our data to be fed into the sklearn function
    features = []
    expected = []
    for x in trainList:
        features.append(dict[x]['features'])
        expected.append(dict[x]['Class'])

    features = pre.normalize(test)  # Normilize the data for processing
    model = MLPClassifier(solver='lbfgs', alpha=1e-5,
                          hidden_layer_sizes=(5, 2), random_state=1).fit(features, expected)
    pred = model.predict(features)

    conMatrix = sklearn.metrics.confusion_matrix(
        expected, model.predict(features))
    print("Artifical Neural Network Confusion Matrix\n", conMatrix, "\n")
    print("Artifical Neural Network Algorithm: ")
    print(sklearn.metrics.classification_report(expected, pred,
                                                target_names=['Male', 'Female'], digits=2))


'''
This function is used to create Naive Bayes Classifier
'''


def nModel(dict, trainList):
    # This peice is to prepare our data to be fed into the sklearn function
    features = []
    expected = []
    for x in trainList:
        features.append(dict[x]['features'])
        expected.append(dict[x]['Class'])

    features = pre.normalize(features)
    model = GaussianNB().fit(features, expected)
    pred = model.predict(features)
    conMatrix = sklearn.metrics.confusion_matrix(expected, pred)

    print("Naive Bayes Confusion Matrix\n", conMatrix, "\n")
    print("Naive Bayes Algorithm: ")
    print(sklearn.metrics.classification_report(expected, pred,
                                                target_names=['Male', 'Female'], digits=2))


''''
Program Start
'''


def main():
    # create a dictionary of people and a list of keys (file name) and
    # the people who will be trained on and tested on
    people, trainList = ReadFile.createArray()

    # add feature calcuations to each persons page
    for key in people:

        # Create a list of the features for a given person to pass to
        # sklearn training list
        people[key]['features'] = [Features.EyeLength(people[key]['x'], people[key]['y']),
                                   Features.EyeDistance(
                                       people[key]['x'], people[key]['y']),
                                   Features.NoseRatio(
                                       people[key]['x'], people[key]['y']),
                                   Features.LipSize(
                                       people[key]['x'], people[key]['y']),
                                   Features.LipLength(
                                       people[key]['x'], people[key]['y']),
                                   Features.EyeBrowLength(
                                       people[key]['x'], people[key]['y']),
                                   Features.Aggression(
                                       people[key]['x'], people[key]['y'])]

        # Assign a class, male or female, to each entry.
        if (key[0] == 'm'):
            people[key]['Class'] = 0
        else:
            people[key]['Class'] = 1
    print("Males Training Sample Set Size: ", 240,
          "Females Training Sample Set Size: ", 165)

    testFeat = []
    for x in trainList:
        testFeat.append(people[x]['features'])

    kModel(people, trainList, testFeat)
    aModel(people, trainList, testFeat)
    nModel(people, trainList)


if __name__ == "__main__":
    main()
