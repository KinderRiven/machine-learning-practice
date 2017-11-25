import matplotlib
import matplotlib.pyplot as plt
from numpy import *
import operator


def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    #print numberOfLines
    #print arrayOLines
    index = 0
    for line in arrayOLines:
        line = line.strip()
        #remove /t /n ...
        #print line
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index +=1
    print returnMat

file2matrix("datingTestSet2.txt")