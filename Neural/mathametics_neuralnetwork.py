# from keras.Layers import Layers
import numpy as np
from tensorflow.keras.activation import Activation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from dense import Dense
from activations import Tanh
from losses import mse, mse_prime
from network import train, predict

class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    
    def Forward (self,input):
        pass

    def Backward(self,output_gradiant, Learning_rate):
        # To update parameter and update Gradient
        input_error = np.dot(output_gradiant, self.weights.T)
        weights_error = np.dot(self.input.T, output_gradiant)
        # dBias = output_error

        # update parameters
        self.weights -= Learning_rate * weights_error
        self.bias -= Learning_rate * output_gradiant
        return input_error

# Y = W X + B

class Dense(Layer):
    def __init__(self,input_size,output_size):
        self.weights = np.random.random(output_size,input_size)
        self.bias = np.random.random(output_size,1)

    def Forward(self,input):
        self.input = input
        return np.dot(self.weights,self.input) + self.bias
    
    def Backward(self, output_gradient,learning_rate):
        weight_gradient = np.dot(output_gradient,self.input.T)
        self.weights -= learning_rate * weight_gradient
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights.T,output_gradient)

class Activation(Layer):
    def __init___(self,activation,activition_prime):
        self.activation = activation
        self.activation_prime =activition_prime

    def Forward(self,input):
        self.input = input
        return self.activation(self.input)
    
    def Backward(self,output_gradient,Learnoing_rate):
        return np.multiply(output_gradient,self.activation_prime(self.input))


class Tanh(Activation):
    def __init___(self):
        tanh = lambda x: np.tanh(x)
        tanh_prime = lambda x : 1-np.tanh(x) **2
        super().__init__(tanh,tanh_prime)

def mse(y_true,y_pred):
    return np.mean(np.power(y_true-y_pred),2)
def mse_prime(y_true,y_pred):
    return 2 * (y_pred - y_true) / np.size(y_true)



X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))

network = [
    Dense(2, 3),
    Tanh(),
    Dense(3, 1),
    Tanh()
]

# train
train(network, mse, mse_prime, X, Y, epochs=10000, learning_rate=0.1)

# decision boundary plot
points = []
for x in np.linspace(0, 1, 20):
    for y in np.linspace(0, 1, 20):
        z = predict(network, [[x], [y]])
        points.append([x, y, z[0,0]])

points = np.array(points)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap="winter")
plt.show()