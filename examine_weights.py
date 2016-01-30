import numpy as np
import numpy.random as npr
import networkx as nx
import gzip
import cPickle
from mlp import create_mnist_samples, onehots
import matplotlib.pyplot as plt

if __name__ == "__main__":
    FILENAME = "weight_mat.npy"
    network_mat = np.abs(np.load(FILENAME))
    max_network_member = np.max(network_mat)
    network_mat /= max_network_member
    # samples, _ = create_mnist_samples()
    # print np.mean(samples['input'][:30000][:, 0])
    print network_mat.shape
    plt.hist(network_mat.ravel())
    plt.show()
    # for x in xrange(30):
    #     plt.close()
    #     plt.hist(network_mat[:, x], bins=30)
    #     plt.gca().set_xscale("log")
    #     plt.gca().set_yscale("log")
    #     plt.show()
