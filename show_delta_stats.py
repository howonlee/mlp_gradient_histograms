import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    print "take abs values of everything"
    print "that is kind of a total cop-out but the code is very simple, and you will wonder at how stupid it is and how you are still seeing a heavy tail"
    FILENAME = "delta.npy"
    delta_mat = np.abs(np.load(FILENAME))
    THRESH = np.median(delta_mat) # something robust, maybe?
    print "thresh: ", THRESH
    weights = []
    for x in xrange(delta_mat.shape[0]):
        weights.append(delta_mat[x] + 1.0)
    print "see if there is a heavy tail in error value distribution"
    print "let's see that weight histogram, in other weights"
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq, bins=30)
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.ylabel("number of errors in histogram bucket")
    plt.xlabel("value of error + 1")
    plt.grid(True)
    plt.title("error value hist plot")
    plt.show()
