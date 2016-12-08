import tensorflow as tf
import numpy as np
import sys

# we get these data from the monkeyrunner module

if len(sys.argv) == 3:
    x_data = np.array(eval(sys.argv[1])).astype(np.float32)
    y_data = np.array(eval(sys.argv[2])).astype(np.float32)
else:
    # these are already farmed data put here just as an example
    x_data = np.array([0.1, 0.11, 0.12000000000000001, 0.13, 0.14, 0.15000000000000002, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21000000000000002, 0.22, 0.23, 0.24000000000000002, 0.25, 0.26, 0.27, 0.28, 0.29000000000000004, 0.3, 0.31, 0.32, 0.32999999999999996, 0.33999999999999997, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.42, 0.43, 0.44, 0.44999999999999996, 0.45999999999999996, 0.47, 0.48, 0.49, 0.5, 0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.5700000000000001, 0.58, 0.59, 0.6, 0.61, 0.62, 0.63, 0.64, 0.65, 0.6599999999999999, 0.6699999999999999, 0.6799999999999999, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.7799999999999999, 0.7899999999999999, 0.8, 0.81, 0.8200000000000001, 0.8300000000000001, 0.8400000000000001 ]).astype(np.float32)
    y_data = np.array([57, 68, 93, 93, 92, 118, 104, 117, 117, 127, 142, 151, 152, 152, 163, 174, 177, 176, 187, 209, 199, 211, 222, 234, 234, 247, 258, 258, 269, 269, 281, 281, 281, 306, 306, 303, 318, 316, 327, 341, 327, 353, 364, 350, 364, 388, 388, 387, 398, 398, 399, 423, 433, 435, 435, 433, 457, 469, 469, 469, 483, 482, 493, 493, 517, 517, 517, 528, 539, 541, 538, 566, 564, 563, 577]).astype(np.float32)

# Try to find values for W and b that compute y_data = W * x_data + b
# (We know that W should be 0.1 and b 0.3, but TensorFlow will
# figure that out for us.)
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    sess.run(train)

wRawValue = float(sess.run(W))
bRawValue = float(sess.run(b))
print (str(wRawValue)+" "+str(bRawValue))