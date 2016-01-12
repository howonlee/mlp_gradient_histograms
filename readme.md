Fractal patterns in backprop gradients for MLP
---

Get mnist.pkl.gz from the theano site or [here](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/data/mnist.pkl.gz), put in in the containing folder willy-nilly.

Run mlp.py, then show_stats.py, you should see a radical inequality that a physicist who hasn't read [Clauset Shalizi Newman 2007](http://arxiv.org/abs/0706.1062) would call a power law. It should just have a heavy tail, anyhow.

If you are piqued by show_stats.py, try fractal_stats.py, which does the comparable looking at the histograms of weights for a weighted ifs-generated fractal (Sierpinski-like thing).

This is BSD-licensed, made by NP Rougier, edited by Howon Lee
