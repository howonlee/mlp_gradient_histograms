import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

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
    network_mat = np.load(FILENAME)
    network = nx.Graph()
    weights = []
    for x in xrange(network_mat.shape[0]):
        for y in xrange(network_mat.shape[1]):
            weights.append(network_mat[x,y])
            #network.add_edge(x, y, weight=network_mat[x,y])
    print "now, see if it percolates and has small world"
##########################
    print "see if power law and/or fat tail in degrees and weights"
    weight_seq = sorted(weights, reverse=True)
    plt.loglog(weight_seq, 'b-')
    plt.title("weight rank plot")
    plt.ylabel("weight")
    plt.xlabel("rank")
    plt.show()
##########################
    print "let's look at clustering coefficients, which I didn't mention in the essay but is pretty easy to understand: the number of triangles"
##########################
    print "inspect recursive structure by looking at the adjacency matrix"
    print "there are more sophisticated methods,"
    print "but you could probably just be convinced by looking at the thing and saying,"
    print "mmm... yep, that there is pretty recursive"
    print "for good measure, let's look at it normal size and zoomed in 2x. normal size:"
    # plt.close()
    # plt.matshow(np.abs(network_mat))
    # plt.colorbar()
    # plt.title("normal size gradient 'network' adj. mat")
    # plt.show()
    print "zoomed in:"
    # net_shape = network_mat.shape
    # plt.close()
    # plt.matshow(np.abs(network_mat[:net_shape[0] // 2, :net_shape[1] // 2]))
    # plt.title("zoomed in gradient 'network' adj. mat")
    # plt.colorbar()
    # plt.show()
    print "it's not an interesting fractal, yes. but it's a fractal."
