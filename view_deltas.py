import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    deltas1 = np.load("delta_0.npy")
    deltas1 = np.abs(deltas1)
    deltas1 /= np.max(deltas1)
    plt.plot(deltas1)
    deltas2 = np.load("delta_50.npy")
    deltas2 = np.abs(deltas2)
    deltas2 /= np.max(deltas2)
    plt.plot(deltas2)
    deltas3 = np.load("delta_100.npy")
    deltas3 = np.abs(deltas3)
    deltas3 /= np.max(deltas3)
    plt.plot(deltas3)
    deltas4 = np.load("delta_400.npy")
    deltas4 = np.abs(deltas4)
    deltas4 /= np.max(deltas4)
    plt.plot(deltas4)
    plt.show()
