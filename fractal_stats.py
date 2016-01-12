import numpy as np
import matplotlib.pyplot as plt

def weighted_sierpinski(order):
    # sort of copied over for typical params for a stochastic kronecker graph
    seed = np.array([[0.99, 0.7], [0.7, 0.1]])
    sierpinski_arr = np.copy(seed)
    for x in xrange(order):
        sierpinski_arr = np.kron(sierpinski_arr, seed)
    return sierpinski_arr

if __name__ == "__main__":
    frac = weighted_sierpinski(10)
    # # if you are piqued and want to see the thing, uncomment the below:
    # plt.imshow(frac)
    # plt.colorbar()
    # plt.show()
    # plt.close()
    frac_mean = np.mean(frac)
    frac += 1.0
    weights = list(frac.ravel())
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq, bins=30, histtype='bar')
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.axis([1, 2, 0, 500000])
    plt.grid(True)
    plt.title("weight hist plot")
    plt.show()
