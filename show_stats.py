import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    print "take abs values of everything"
    print "it is kind of a total cop-out but the code is very simple, and you will wonder at how stupid it is and how you are still seeing a heavy tail"
    FILENAME = "weight_mat.npy"
    mat = np.abs(np.load(FILENAME))
    THRESH = np.median(mat) # something robust, maybe?
    print "thresh: ", THRESH
    weights = []
    for x in xrange(mat.shape[0]):
        for y in xrange(mat.shape[1]):
            weights.append(mat[x,y] + 1.0)
    print "see if there is a heavy tail in weight distribution"
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq, bins=30)
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.ylabel("number of weights in histogram bucket")
    plt.xlabel("value of weight + 1")
    plt.grid(True)
    plt.title("weight value hist plot")
    plt.show()
