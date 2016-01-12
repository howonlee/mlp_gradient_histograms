import numpy as np
import numpy.random as npr
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    FILENAME = "grad_mat.npy"
    network_mat = np.abs(np.load(FILENAME))
    max_network_member = np.max(network_mat)
    network_mat /= max_network_member
    network = nx.Graph()
    for x in xrange(network_mat.shape[0]):
        for y in xrange(network_mat.shape[1]):
            if network_mat[x,y] > npr.rand():
                network.add_edge(x, y, weight=network_mat[x,y])
    degree_sequence = sorted(nx.degree(network).values(),reverse=True)
    plt.hist(degree_sequence, 60)
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.axis([1, 1000, 0, 1000])
    plt.grid(True)
    plt.show()
