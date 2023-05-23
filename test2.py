import tensorflow as tf
import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    error = tf.abs(y_true - y_pred)
    quadratic = tf.minimum(error, delta)
    linear = (error - quadratic)
    return tf.reduce_mean(0.5 * tf.square(quadratic) + delta * linear)
    #return tf.where(error < delta, 0.5 * tf.square(quadratic), delta * linear)

true = np.array([-10, 1, 2])
pred = np.array([-10, 1.5, 4])
loss = huber_loss(true, pred)
print(loss)
