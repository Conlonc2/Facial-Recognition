''' This file will be used to calculate features of each person. '''
#-Imports-#
import math

'''
Calculate distance between every point and take an average [Test Feature NOT to be kept in]
'''


def fullerCalc(x, y):
    inter = len(x)
    temp = []

    for i in range(inter):
        for j in range(inter):
            temp.append(
                math.sqrt(math.pow(x[i] - x[j], 2) + math.pow(y[i]-y[j], 2)))
    toReturn = sum(temp) / len(temp)

    return(toReturn)


'''
Eye length ratio: length of eye (maximum of two) over distance between points 8 and 13.
'''


# (x8, x9, x10, x11, x12, x13, y8, y9, y10, y11, y12, y13):
def EyeLength(x, y):
    numerator = math.sqrt(math.pow(x[9] - x[10], 2) + math.pow(y[9]-y[10], 2))  \
        + math.sqrt(math.pow(x[11]-x[12], 2) + math.pow(y[11]-y[12], 2))
    denom = math.sqrt(
        (math.pow((x[8] - x[13]), 2)) + (math.pow((y[8] - y[13]), 2)))
    return (numerator/denom)


'''
Eye distance ratio: distance between center of two eyes over distance
between points 8 and 13.
'''


def EyeDistance(x, y):
    numerator = math.sqrt(math.pow(x[0]-x[1], 2) + math.pow(y[0]-y[1], 2))
    denom = math.sqrt(
        (math.pow((x[8] - x[13]), 2)) + (math.pow((y[8] - y[13]), 2)))
    return (numerator / denom)


'''
Nose ratio: Distance between points 15 and 16 over distance between 20 and 21.
'''


def NoseRatio(x, y):
    numerator = math.sqrt(math.pow(x[15]-x[16], 2) + math.pow(y[15]-y[16], 2))
    denom = math.sqrt(math.pow(x[20]-x[21], 2) + (math.pow(y[20]-y[21], 2)))

    return (numerator/denom)


'''
Lip size ratio: Distance between points 2 and 3 over distance between 17 and 18.
'''


def LipSize(x, y):
    numerator = math.sqrt(math.pow(x[2]-x[3], 2) + math.pow(y[2]-y[3], 2))
    denom = math.sqrt(math.pow(x[17]-x[18], 2) + (math.pow(y[17]-y[18], 2)))

    return (numerator/denom)


'''
Lip length ratio: Distance between points 2 and 3 over distance between 20 and 21.
'''


def LipLength(x, y):
    numerator = math.sqrt(math.pow(x[2]-x[3], 2) + math.pow(y[2]-y[3], 2))
    denom = math.sqrt(math.pow(x[20]-x[21], 2) + (math.pow(y[20]-y[21], 2)))

    return (numerator/denom)


'''
Eye-brow length ratio: Distance between points 4 and 5
(or distance between points 6 and 7 whichever is larger)
over distance between 8 and 13.
'''


def EyeBrowLength(x, y):
    ''' Decide what distance is greater and store that value as the numerator.'''
    if (math.sqrt(math.pow(x[4]-x[5], 2) + math.pow(y[4]-y[5], 2)) >
            math.sqrt(math.pow(x[6]-x[7], 2) + math.pow(y[6]-y[7], 2))):

        numerator = math.sqrt(math.pow(x[4]-x[5], 2) + math.pow(y[4]-y[5], 2))
    else:
        numerator = math.sqrt(math.pow(x[6]-x[7], 2) + math.pow(y[6]-y[7], 2))

    denom = math.sqrt(math.pow(x[8]-x[13], 2) + (math.pow(y[8]-y[13], 2)))

    return (numerator/denom)


'''
Aggressive ratio: Distance between points 10 and 19 over distance between 20 and 21.
'''


def Aggression(x, y):
    numerator = math.sqrt(math.pow(x[10]-x[19], 2) + math.pow(y[10]-y[19], 2))
    denom = math.sqrt(math.pow(x[20]-x[21], 2) + (math.pow(y[20]-y[21], 2)))

    return (numerator/denom)
