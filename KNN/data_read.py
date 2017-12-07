import csv
from numpy import *

data_file = open("test.csv", "r")
csv_reader = csv.reader(data_file)
cnt = 0
size = 0
for line in csv_reader:
    print line
    cnt = cnt + 1
    if cnt > 2:
        matrix = mat(line)
        size = matrix.shape[1]
        vector = matrix.reshape(matrix.shape[1], matrix.shape[0])
        break
matrix = mat(random.rand(size, size))
vector = mat(random.rand(size, 1))
print matrix.shape
print vector.shape
print matrix * vector