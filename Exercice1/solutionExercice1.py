import numpy as np
from math import *


def model(X, W, b):
    som = 0
    for i in range(len(X)):
        som = som + X[i]*W[i]
    Z1 = som + b
    return Z1

def activation(f):
    if f>0:
        return f
    else:
        return 0
    
"""Couche cache: fonction ReLU(fonction redresseur)   
def ReLU(f):
    return f * (f > 0)

def dReLU(x):
    return 1. * (x > 0)    
"""

def linreg_next_layer(f1, f2, f3, W4):
    somf = 0
    for z in W4:
        somf = f1*z + f2*z + f2*z + b4
    return somf

#sigmoide la valeur change entre 0 et 1
def sigmoide(f5):
    return 1 / (1 + np.exp(-f5))

X = [1,-3.1,-7.2, 2.1]
W = [2.1, 1.2, 0.3, 1.3]
b = -3
W2 = [0.1, 1.2, 4.9, 3.1]
b2 = -5
X = [1,-3.1,-7.2, 2.1]
W3 = [0.4, 2.6, 2.5, 3.8]
b3 = -8
W4 = [1.1, -4.1,0.7]
b4 = 5.1

f1 = model(X, W, b)
print("premiere sortie :",f1)
A1 = activation(f1)
print("activation(f1) :",A1)


f2 = model(X, W2,b2)
print("deuxieme sortie : ",f2)
A2 = activation(f2)
print("Activation(f2) :", A2)


f3 = model(X, W3, b3)
print("troisieme sortie : ",f3)
A3 = activation(f3)
print("Activation(f3):", A3)
    
f5 = linreg_next_layer(f1, f2, f3, W4)
print("Deuxieme couche :",f5) 
A4 = sigmoide(f5)
print("valeur final :", A4)
            




