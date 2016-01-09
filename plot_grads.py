import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    grads = []
    with open("grads") as grads_file:
        for line in grads_file:
            try:
                grads.append(abs(float(line)) + 1)
            except:
                pass
    plt.hist(grads, bins=np.logspace(0.001, 0.05, 50))
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.axis([1, 1.1, 0, 40000])
    plt.show()
