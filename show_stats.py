import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    print "take abs values of everything"
    print "it is kind of a total cop-out but the code is very simple, and you will wonder at how stupid it is"
    FILENAME = "grad_mat.npy"
    network_mat = np.abs(np.load(FILENAME))
    THRESH = np.mean(network_mat) # something robust, maybe?
    print THRESH
    network = nx.Graph()
    weights = []
    for x in xrange(network_mat.shape[0]):
        for y in xrange(network_mat.shape[1]):
            weights.append(network_mat[x,y] + 1.0)
            if network_mat[x,y] > THRESH:
                network.add_edge(x, y, weight=network_mat[x,y])
    print "see if power law and/or fat tail in weights"
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq, bins=30, facecolor='blue', histtype='bar') # plt.plot(weight_seq, 'b-')
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.axis([1, 1 + (THRESH * 50.0), 0, 40000])
    plt.grid(True)
    plt.title("weight hist plot")
    plt.show()
