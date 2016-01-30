import numpy as np
import numpy.random as npr
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    FILENAME = "weight_mat.npy"
    network_mat = np.abs(np.load(FILENAME))
    max_network_member = np.max(network_mat)
    print "this is not really something you are supposed to do, I think"
    print "but it is quite interesting."
    print "take the weight matrix, normalize it so that the biggest single member of that matrix is 1"
    network_mat /= max_network_member
    for x in xrange(30):
        plt.close()
        plt.hist(network_mat.T[:, x])
        plt.show()
