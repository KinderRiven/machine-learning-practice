import csv
import numpy as np

train_file = open("train.csv", "r")
csv_reader = csv.reader(train_file)
array = []
index = 0
for line in csv_reader:
    if index > 88:
        print line
        array = line[1:]
        break
    index = index + 1

img = np.array(array).reshape(28, 28)
for line in img:
    for each in line:
        each = each.zfill(3)
        print each,
    print '\n'