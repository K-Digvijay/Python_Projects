import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("train.csv")

data = np.array(data)
m,n = data.shape
np.random.shuffle(data)

data_dev = data[0:1000].T

y_dev = data_dev[0]
X_dev = data_dev[1:n]

data_train = data[1000:m].T
y_train = data_train[0]
X_train = data_train[1:n]

def init_params():
    W1 = np.random.randn(10,784) - 0.5
    b1 = np.random.randn(10,1) - 0.5
    W2 = np.random.randn(10,10) -0.5
    b2 = np.random.randn(10,1)- 0.5

    return W1,b1,W2,b2

def Relu(Z):
    return np.maximum(0,Z)

def softmax(Z):
    expz = np.exp(Z - np.max(Z,axis = 0, keepdims = True))
    return expz / np.sum(expz,axis = 0, keepdims  = True)

def forward_prop(W1,b1,W2,b2,X):
    Z1 = W1.dot(X) + b1
    A1 = Relu(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1,A1,Z2,A2

def deriv_Relu(z):
    return z > 0

def onehot(y):
    onehot_y = np.zeros((y.size,y.max() +1))
    onehot_y[np.arange(y.size),y] = 1
    onehot_y = onehot_y.T
    return onehot_y

def back_prop(Z1,A1,Z2,A2,W1,W2,X,Y):
    m = Y.size
    onehot_y = onehot(Y)
    dz2 = A2 - onehot_y
    dw2 = 1 / m* dz2.dot(A1.T)
    db2 = 1 / m* np.sum(dz2)
    dz1 = W2.T.dot(dz2) * deriv_Relu(Z1)
    dw1 = 1 / m * dz1.dot(X.T)
    db1 = 1 / m * np.sum(dz1)
    return dw1,db1,dw2,db2

def update_params(w1,b1,w2,b2,dw1,db1,dw2,db2,alpha):
    w1 = w1 - alpha * dw1
    b1 = b1 - alpha * db1
    w2 = w2 - alpha * dw2
    b2 = b2 - alpha * db2
    return w1,b1,w2,b2

def get_prediction(a2):
    return np.argmax(a2,0)

def get_accuracy(prediction,y):
    print(prediction,y)
    return np.sum(prediction == y) / y.size

def gadient_descent(x,y,alpha,iter):
    w1,b1,w2,b2 = init_params()
    for i in range(iter):
        z1,a1,z2,a2 = forward_prop(w1,b1,w2,b2,x)
        dw1,db1,dw2,db2 = back_prop(z1,a1,z2,a2,w1,w2,x,y)
        w1,b1,w2,b2 = update_params(w1,b1,w2,b2,dw1,db1,dw2,db2,alpha)
        if i % 20 == 0:
            print(f"Iteration: {i} Accuracy: {get_accuracy(get_prediction(a2),y)}")
    return w1,b1,w2,b2


w1,b1,w2,b2 = gadient_descent(X_train,y_train,0.1,100)















