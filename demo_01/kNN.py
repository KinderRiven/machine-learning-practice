from numpy import *
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    #print dataSetSize
    #lie dataSetSize | hang 1
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    #print diffMat
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    print distances
    #return index
    sortedDistIndeicies = distances.argsort()
    #print sortedDistIndeicies
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndeicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount


group, labels = createDataSet()
print group
print labels
print classify0([0, 0], group, labels, 3)

