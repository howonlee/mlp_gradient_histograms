import numpy as np
import networkx as nx

if __name__ == "__main__":
    FILENAME = "grad_mat.npy"
    network_mat = np.abs(np.load(FILENAME))
    THRESH = np.mean(network_mat)
    network = nx.Graph()
    for x in xrange(network_mat.shape[0]):
        for y in xrange(network_mat.shape[1]):
            if network_mat[x,y] > THRESH:
                network.add_edge(x, y, weight=network_mat[x,y])
    degree_sequence = sorted(nx.degree(network).values(),reverse=True)
    print degree_sequence
