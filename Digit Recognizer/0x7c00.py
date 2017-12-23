import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D
from keras.optimizers import SGD, Adam
from keras.utils.vis_utils import *
import numpy as np
import csv


def file2matrix(filename, rtype):
    train_file = open(filename, "r")
    csv_reader = csv.reader(train_file)
    ret_mat = []
    ret_class = []
    index = 0
    for line in csv_reader:
        if rtype == 'train' and index > 0:
            ret_mat.append(line[1:])
            ret_class.append(int(line[0]))
        elif rtype == 'test' and index > 0:
            ret_mat.append(line[0:])
        index = index + 1
    return ret_mat, ret_class

num_classes = 10
units = 500
batch_size = 200
nb_epoch = 60
image_x = 28
image_y = 28

x_train, y_train = file2matrix('train.csv', 'train')
x_test, y_test = file2matrix('test.csv', 'test')

x_train = np.array(x_train)
x_train = x_train.reshape(x_train.shape[0], image_x, image_y)
y_train = np.array(y_train)

x_test = np.array(x_test)
x_test = x_test.reshape(x_test.shape[0], image_x, image_y)
y_test = np.array(y_test)

print x_train.shape, y_train.shape

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()

model.add(Conv2D(filters=32, input_shape=x_train.shape[1:], padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(filters=32))

result_file = open("sample_submission.csv", "w")
result_writer = csv.writer(result_file)
header = ["imageId", "Label"]
index = 0
result_writer.writerow(header)
