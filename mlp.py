#!/usr/bin/env python
# -----------------------------------------------------------------------------
# Multi-layer perceptron
# Copyright (C) 2011  Nicolas P. Rougier
#
# Distributed under the terms of the BSD License.

# shamelessly taken and modified by Howon Lee in 2016, cuz BSD allows that
# only Howon doesn't know which version of the BSD license Howon should replicate
# so whatever version NP Rougier wanted, consider it replicated
# dont think that NP Rougier has heard of Howon, because he prolly hasn't
# nor vice versa, now that Howon thinks about it
# -----------------------------------------------------------------------------

# This is an implementation of the multi-layer perceptron with retropropagation
# learning.

# modified by Howon Lee to make a point about the fractal nature of backprop
# play with the params as you like
# -----------------------------------------------------------------------------
import numpy as np
import cPickle
import gzip

def sigmoid(x):
    ''' Sigmoid like function using tanh '''
    return np.tanh(x)

def dsigmoid(x):
    ''' Derivative of sigmoid above '''
    return 1.0-x**2

class MLP:
    '''
    Multi-layer perceptron class.
    This is used via SGD only in the MNIST thing Howon rigged up
    '''

    def __init__(self, *args):
        ''' Initialization of the perceptron with given sizes.  '''

        self.shape = args
        n = len(args)

        # Build layers
        self.layers = []
        # Input layer (+1 unit for bias)
        self.layers.append(np.ones(self.shape[0]+1))
        # Hidden layer(s) + output layer
        for i in range(1,n):
            self.layers.append(np.ones(self.shape[i]))

        # Build weights matrix (randomly between -0.25 and +0.25)
        self.weights = []
        for i in range(n-1):
            self.weights.append(np.zeros((self.layers[i].size,
                                         self.layers[i+1].size)))

        # dw will hold last change in weights (for momentum)
        self.dw = [0,]*len(self.weights)

        # Reset weights
        self.reset()

    def reset(self):
        ''' Reset weights '''

        for i in range(len(self.weights)):
            Z = np.random.random((self.layers[i].size,self.layers[i+1].size))
            self.weights[i][...] = (2*Z-1)*0.25

    def propagate_forward(self, data):
        ''' Propagate data from input layer to output layer. '''

        # Set input layer
        self.layers[0][0:-1] = data

        # Propagate from layer 0 to layer n-1 using sigmoid as activation function
        for i in range(1,len(self.shape)):
            # Propagate activity
            self.layers[i][...] = sigmoid(np.dot(self.layers[i-1],self.weights[i-1]))

        # Return output
        return self.layers[-1]


    def propagate_backward(self, target, lrate=0.1, momentum=0.1, filename="grad_mat"):
        ''' Back propagate error related to target using lrate. '''

        deltas = []

        # Compute error on output layer
        error = target - self.layers[-1]
        delta = error*dsigmoid(self.layers[-1])
        deltas.append(delta)

        # Compute error on hidden layers
        for i in range(len(self.shape)-2,0,-1):
            delta = np.dot(deltas[0],self.weights[i].T)*dsigmoid(self.layers[i])
            deltas.insert(0,delta)

        # Update weights
        for i in range(len(self.weights)):
            layer = np.atleast_2d(self.layers[i])
            delta = np.atleast_2d(deltas[i])
            dw = np.dot(layer.T,delta)
            if i == 0:
                np.save(filename, dw)
                print "dw saved"
            self.weights[i] += lrate*dw + momentum*self.dw[i]
            self.dw[i] = dw

        # Return error
        return (error**2).sum()


# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import matplotlib
    import matplotlib.pyplot as plt

    def bitfield(n):
        """
        Don't care about the MLP results, so don't care about the output patterns
        So let's do this
        """
        return np.array([n >> i & 1 for i in range(7,-1,-1)])

    def create_samples(filename="mnist.pkl.gz"):
        # only 500 datapoints, we don't even really need that many
        # we are not using this net, so can just use training only
        samples = np.zeros(50000, dtype=[('input',  float, 784), ('output', float, 8)])
        with gzip.open(filename, "rb") as f:
            train_set, valid_set, test_set = cPickle.load(f)
            for x in xrange(50000):
                samples[x] = train_set[0][x], bitfield(train_set[1][x])
        return samples

    print "MNIST, friendo"
    network = MLP(784, 784, 8)
    samples = create_samples()
    for i in range(100):
        print "pattern: ", i
        n = np.random.randint(samples.size)
        network.propagate_forward(samples['input'][n])
        network.propagate_backward(samples['output'][n])
    print "and then we don't use the net for anything"
