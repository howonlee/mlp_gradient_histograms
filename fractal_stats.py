import numpy as np

def chaos_game(dim):
    pass

if __name__ == "__main__":
    frac = chaos_game(512)
    frac_mean = np.mean(frac) # not robust, ah well
    weights = list(frac.ravel)
    weight_seq = sorted(weights, reverse=True)
    plt.hist(weight_seq, bins=30, histtype='bar')
    plt.gca().set_xscale("log")
    plt.gca().set_yscale("log")
    plt.axis([1, 1 + (frac_mean * 50.0), 0, 40000])
    plt.grid(True)
    plt.title("weight hist plot")
    plt.show()
