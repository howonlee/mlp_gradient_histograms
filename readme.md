Fractal patterns in backprop gradients for MLP
---

Get mnist.pkl.gz from the theano site or [here](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/data/mnist.pkl.gz), put in in the containing folder willy-nilly. If you want the CIFAR samples, get that [data](https://www.cs.toronto.edu/~kriz/cifar.html). CIFAR-10, mind you. Take it out of gzip and put it in a folder called `cifar-10-batches-py`.

I don't have a proper requirements.txt but new numpy, matplotlib, networkx should be all you need.

Run `mlp.py`, then `show_stats.py`, you should see a radical inequality that a physicist who hasn't read [Clauset Shalizi Newman 2007](http://arxiv.org/abs/0706.1062) would call a power law. It should just have a heavy tail, anyhow. Now, try it with the random samples (there's a function called create_random_samples). Then, try it with the CIFAR samples (it's just one color from CIFAR - in a function called create_cifar_samples). I am greatly amused myself by the fact that it loses the shape it has in the random samples. Jeff was quite alarmed about the seeming squareness on the pattern, but look at the reaction to CIFAR.

There is often a zeroing-out numerical problem, especially with the random samples, because the network gets into a corner.

If you are piqued by `show_stats.py`, try `fractal_stats.py`, which does the comparable looking at the histograms of weights for a weighted ifs-generated fractal (Sierpinski-like thing, but with typical-ish parameter for a stochastic kronecker graph. I was always amused by the strange sameness of the parameters they got for radically different networks).

If you are piqued by _that_, try `grad_network.py`, which takes the gradient for one SGD step from mlp.py and tries turning it into a network. That network looks suspiciously like a social network (complex network). Also look at `weight_network.py`, which does the same for the weights for a whole trained multilayer perceptron, showing that this "induced weight network" is _not_ a complex network. Compare the network you get from `weight_network.py` to section IV.A of MEJ Newman's review of power laws. Sole et al I think have a definition for informational quantities _on_ networks (entropy, mutual information, etc), I forget if it's the only good one, but it's a good one.

This is BSD-licensed, made by NP Rougier, edited by Howon Lee. Thanks to Jeff Shrager for helping me poking at it.

I'm working on seeing if a similar thing holds for the gradient approximations contrastive divergence gives you in an RBM.
