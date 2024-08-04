import numpy as np
import pandas as pd
import scipy
from scipy import linalg
from sklearn.datasets import load_breast_cancer

data = np.array([1, 2, 3, 4, 5])
print(data)
print(len(data))
print(type(data))
print(data.shape)

data = np.array(['g', 'a', 'u', 'r', 'a', 'v'])
s = pd.Series(data)
print(s)

A = np.array([[1, 2], [3, 4]])
print(linalg.inv(A))

data = load_breast_cancer()
print(data.target[[10, 50, 85]])
print(list(data.target_names))

import tensorflow as tf

data = tf.constant([[2, 1], [4, 6]])
print(data)

import keras

(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


import matplotlib.pyplot as plt
plt.plot([1,2,3],[1,2,3])
plt.show()

