import tensorflow as tf
import numpy as np


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weight = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Sum = tf.matmul(inputs, Weight) + biases
    if activation_function is None:
        outputs = Sum
    else:
        outputs = activation_function(Sum)
    return outputs

#data
data_num = 300
x_data = np.random.rand(data_num, 1).astype('float32')
y_data = np.sqrt(x_data) + 0.5

#create model
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])

l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
prediction = add_layer(l1, 10, 1, activation_function=None)
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

for _ in range(1000):
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if _ % 100 == 0:
        print(sess.run(loss, feed_dict={xs: x_data, ys: y_data}))