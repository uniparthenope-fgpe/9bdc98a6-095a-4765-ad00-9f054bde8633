import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

# Generate some random data
x_train = np.array([1, 2, 3, 4, 5])
y_train = np.array([2, 4, 6, 8, 10])

# Define the model
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
W = tf.Variable(0.0, name="weight")
b = tf.Variable(0.0, name="bias")
y_pred = X * W + b

# Define the loss function and optimizer
loss = tf.reduce_mean(tf.square(y_pred - Y))
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# Train the model
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for i in range(1000):
        sess.run(optimizer, feed_dict={X: x_train, Y: y_train})
    W_final, b_final = sess.run([W, b])
    print("Final weights:", W_final)
    print("Final bias:", b_final)
