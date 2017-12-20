import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
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

x_train, y_train = file2matrix('train.csv', 'train')
x_test, y_test = file2matrix('test.csv', 'test')

x_train = np.array(x_train).astype(np.float32)
y_train = np.array(y_train).astype(np.float32)

x_test = np.array(x_test).astype(np.float32)
y_test = np.array(y_test).astype(np.float32)

x_test /= 255
x_train /= 255

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print x_train.shape, y_train.shape
print x_test.shape, y_test.shape

model = Sequential()
model.add(Dense(units=units, activation=Activation('relu'),
                input_shape=x_train.shape[1:]))

model.add(Dense(units=units, activation=Activation('relu')))

model.add(Dense(units=units, activation=Activation('relu')))

model.add(Dense(num_classes, activation=Activation('softmax')))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

plot_model(model=model, to_file='test.png', show_shapes=True)
model.fit(x_train, y_train, batch_size=batch_size, nb_epoch=nb_epoch)
#score = model.evaluate(x_test, y_test)
#print score
result = model.predict(x_test)
#print result
result_file = open("sample_submission.csv", "w")
result_writer = csv.writer(result_file)
header = ["imageId", "Label"]
index = 0
result_writer.writerow(header)
for line in result:
    max_value = line[0]
    result = 0
    for i in range(1, len(line)):
        if line[i] > max_value:
            result = i
            max_value = line[i]
    index = index + 1
    print index, result
    result_writer.writerow([index, result])

