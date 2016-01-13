Fractal patterns in backprop gradients for MLP
---

Get mnist.pkl.gz from the theano site or [here](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/data/mnist.pkl.gz), put in in the containing folder willy-nilly.

Run `mlp.py`, then `show_stats.py`, you should see a radical inequality that a physicist who hasn't read [Clauset Shalizi Newman 2007](http://arxiv.org/abs/0706.1062) would call a power law. It should just have a heavy tail, anyhow.

If you are piqued by `show_stats.py`, try `fractal_stats.py`, which does the comparable looking at the histograms of weights for a weighted ifs-generated fractal (Sierpinski-like thing).

If you are piqued by _that_, try `grad_network.py`, which takes the gradient for one SGD step from mlp.py and tries turning it into a network. That network looks suspiciously like a social network (complex network). Also look at `weight_network.py`, which does the same for the weights for a whole trained multilayer perceptron, showing that this "induced weight network" is _not_ a complex network. Compare to section IV.A of MEJ Newman's review of power laws.

This is BSD-licensed, made by NP Rougier, edited by Howon Lee
