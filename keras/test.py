import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils.vis_utils import *


num_classes = 10
units = 500
batch_size = 200
nb_epoch = 3


(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], x_train.shape[1]*x_train.shape[2])
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1]*x_test.shape[2])

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

print x_train.shape, y_train.shape
print x_test.shape, y_test.shape
print x_train.shape[1:]

model = Sequential()
model.add(Dense(units=units, activation=Activation('relu'),
                input_shape=x_train.shape[1:]))

model.add(Dense(units=units, activation=Activation('relu')))

model.add(Dense(units=units, activation=Activation('relu')))

model.add(Dense(num_classes, activation=Activation('softmax')))

model.summary()

model.compile(loss='mse',
              optimizer=SGD(lr=0.1),
              metrics=['accuracy'])

plot_model(model=model, to_file='test.png', show_shapes=True)
model.fit(x_train, y_train, batch_size=batch_size, nb_epoch=nb_epoch)
score = model.evaluate(x_test, y_test)
print score
result = model.predict(x_test)
print result