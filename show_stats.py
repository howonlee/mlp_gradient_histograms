import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == "__main__":
    print "take abs values of everything"
    print "it is kind of a total cop-out but the code is very simple, and you will wonder at how stupid it is and how you are still seeing a heavy tail"
    FILENAME = "grad_mat.npy"
    gradient_mat = np.abs(np.load(FILENAME))
    THRESH = np.median(gradient_mat) # something robust, maybe?
    print "thresh: ", THRESH
    weights = []
    for x in xrange(gradient_mat.shape[0]):
        for y in xrange(gradient_mat.shape[1]):
            weights.append(gradient_mat[x,y] + 1.0)
    print "see if there is a heavy tail in gradient value distribution"
    print "let's see that weight histogram, in other weights"
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq, bins=30)
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.ylabel("number of gradients in histogram bucket")
    plt.xlabel("value of gradient + 1")
    plt.grid(True)
    plt.title("gradient value hist plot")
    plt.show()
