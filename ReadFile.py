''' Functions required to read data(.pts) files. '''
#-Imports-#
import os

'''
Go through the selected direcotry and add all files to an array for later use.
'''


def ReadFiles(path):

    array = []

    for root, _dirs, files in os.walk(path, topdown=False, followlinks=True):
        for name in files:
            array.append(os.path.join(root, name))

    del array[-1]  # remove the dummy.pts file from the list

    return array


'''
Create the array of people with there coordinates in a list of lists
(i.e. person one is index 0, so list[0] returns a list of
coordinates for person 1)
'''


def createArray():
    nameList = []  # will contain ALL samples in our data set
    trainList = []  # will contain ONLY the training set
    testList = []  # will contain ONLY the testing set
    mCount = 0
    fCount = 0
    people = {}
    path = "C:/Users/chris/Desktop/School" \
        "/Programs - Python/A.I/Facial Recognition/points_22"
    files = ReadFiles(path)

    for x in files:
        name = x[-12:-4]  # takes the folder name and uses that as key to dictionary
        if (name[0] == 'm' and mCount < 240):
            trainList.append(name)
            mCount += 1
        elif (name[0] == 'w' and fCount < 165):
            trainList.append(name)
            fCount += 1
        else:
            testList.append(name)
        nameList.append(name)
        temp = open(x, 'r')
        xTemp = []
        yTemp = []
        for line in temp:
            line = line.rstrip()
            token = line.split()
            if (token[0] == "{" or token[0] == "}" or token[0] == 'version:' or
                    token[0] == 'n_points:'):
                continue
            else:
                # create the list of (x,y)Corridnates for a given person
                xTemp.append(float(token[0]))
                yTemp.append(float(token[1]))
        # Create a dictionary where the name refrences a list of X and Y coordinates
        # i.e. print 'name' will print all (x,y) coordinates for a given file
        people[name] = {'x': xTemp, 'y': yTemp}
        temp.close()
    return (people, trainList)
