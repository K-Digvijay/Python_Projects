import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def Forward(self, input):
        pass

    def Backward(self, output_gradient, learning_rate):
        pass


class Dense(Layer):
    def __init__(self, input_size, output_size):
        self.weights = np.random.rand(output_size, input_size)
        self.bias = np.random.rand(output_size, 1)

    def Forward(self, input):
        self.input = input
        return np.dot(self.weights, self.input) + self.bias

    def Backward(self, output_gradient, learning_rate):
        weights_gradient = np.dot(output_gradient, self.input.T)
        self.weights -= learning_rate * weights_gradient
        self.bias -= learning_rate * output_gradient
        return np.dot(self.weights.T, output_gradient)


class Activation(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def Forward(self, input):
        self.input = input
        return self.activation(self.input)

    def Backward(self, output_gradient, learning_rate=None):
        return output_gradient * self.activation_prime(self.input)


class Tanh(Activation):
    def __init__(self):
        tanh = lambda x: np.tanh(x)
        tanh_prime = lambda x: 1 - np.tanh(x) ** 2
        super().__init__(tanh, tanh_prime)


def mse(y_true, y_pred):
    return np.mean(np.power(y_true - y_pred, 2))


def mse_prime(y_true, y_pred):
    return 2 * (y_pred - y_true) / y_true.size


def train(network, loss, loss_prime, X, Y, epochs, learning_rate):
    for epoch in range(epochs):
        error = 0
        for x, y in zip(X, Y):
            # Forward pass
            output = x
            for layer in network:
                output = layer.Forward(output)

            # Compute loss
            error += loss(y, output)

            # Backward pass
            gradient = loss_prime(y, output)
            for layer in reversed(network):
                gradient = layer.Backward(gradient, learning_rate)

        if (epoch + 1) % 100 == 0:
            print(f"Epoch {epoch + 1}/{epochs}, Error: {error}")


def predict(network, input_data):
    output = input_data
    for layer in network:
        output = layer.Forward(output)
    return output


# XOR Problem Dataset
X = np.reshape([[0, 0], [0, 1], [1, 0], [1, 1]], (4, 2, 1))
Y = np.reshape([[0], [1], [1], [0]], (4, 1, 1))

network = [
    Dense(2, 3),
    Tanh(),
    Dense(3, 1),
    Tanh()
]

# Train the network
train(network, mse, mse_prime, X, Y, epochs=10000, learning_rate=0.01)

# Decision boundary plot
points = []
for x in np.linspace(0, 1, 20):
    for y in np.linspace(0, 1, 20):
        z = predict(network, [[x], [y]])
        points.append([x, y, z[0, 0]])

points = np.array(points)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c=points[:, 2], cmap="winter")
plt.show()
