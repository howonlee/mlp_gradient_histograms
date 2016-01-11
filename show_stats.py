import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    print "we are doing a sort of seedy thing, which I like to call in my head networkification"
    print "it gets done a little by recurrence matrix analysts trying to get networks out of time series"
    print "but it's pretty easy and nice to do when we have nice matrices of gradients, since we can sort of treat them as causal relations anyhow"
    print "1. take absolute values of gradients. you can also just take positive or negative gradients, there's no real theoretical basis for this"
    print "2. below a threshhold, say that an relation between two nodes in the multilayer perceptron is not 'in the network'"
    print "3. obviously, the weight semantics of the network are the gradient semantics."
    print "4. now you have a network, now go look at it to see if it's a complex network"
    print "if that explanation is not good enough, just look at the code. Usually, people say that sort of thing as a cop-out."
    print "it is kind of a total cop-out but the code is very simple, and you will wonder at how stupid it is"
    FILENAME = "grad_mat.npy"
    network_mat = np.abs(np.load(FILENAME))
    THRESH = np.mean(network_mat) # something robust, maybe?
    network = nx.Graph()
    weights = []
    for x in xrange(network_mat.shape[0]):
        for y in xrange(network_mat.shape[1]):
            weights.append(network_mat[x,y] + 1)
            if network_mat[x,y] > THRESH:
                network.add_edge(x, y, weight=network_mat[x,y])
    print "now, see if it percolates and has small world"
    print "see if power law and/or fat tail in degrees and weights"
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq) # plt.plot(weight_seq, 'b-')
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.axis([1, 1.00000000005, 0, 40000])
    plt.title("weight hist plot")
    plt.show()

    print "the mere degree plot is pretty disappointing, but it's disappointing in a very familiar way"
    print "let's look at clustering coefficients, which I didn't mention in the essay but is pretty easy to understand: the number of triangles"
##########################
