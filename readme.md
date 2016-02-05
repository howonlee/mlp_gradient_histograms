Fractal patterns in backprop gradients for MLP
---

I am actively experimenting upon this stuff, so these instructions may all be out of date.

Get mnist.pkl.gz from the theano site or [here](https://github.com/mnielsen/neural-networks-and-deep-learning/blob/master/data/mnist.pkl.gz), put in in the containing folder willy-nilly. If you want the CIFAR samples, get that [data](https://www.cs.toronto.edu/~kriz/cifar.html). CIFAR-10, mind you. Take it out of gzip and put it in a folder called `cifar-10-batches-py`.

I don't have a proper requirements.txt but new numpy, matplotlib, networkx should be all you need.

Run `mlp.py`, then `show_stats.py`, you should see a radical inequality in the weights construed as individual weights that someone who hasn't read [Clauset Shalizi Newman 2007](http://arxiv.org/abs/0706.1062) would call a power law. It should just have a heavy tail, anyhow, I think it may be a stretched exponential(likelihood tests forthcoming...). Now, try it with the random samples (there's a function called create_random_samples). Then, try it with the CIFAR samples (in a function called create_cifar_samples). I am greatly amused myself by the fact that it loses the shape it has in the random samples. Jeff was quite alarmed about the seeming squareness on the pattern, but look at CIFAR.

There is often a zeroing-out numerical problem, especially with the random samples, because the network gets into a corner. I will leave it as is because I haven't decided on the proper way to interact with the absolute valuation I'm doing. One valid criticism is that I'm taking absolute values and saying nothing about them, which I definitely need to look into

If you are piqued by `show_stats.py`, try `fractal_stats.py`, which does the comparable looking at the histograms of a "gradient" for a weighted ifs-generated fractal (Sierpinski-like thing, but with typical-ish parameter for a stochastic kronecker graph. I was always amused by the strange sameness of the parameters they got for radically different networks).

If you are piqued by _that_, try `weight_network.py`, which takes the weights from mlp.py and tries turning it into a network by the unscrupulous ensemble-sampling way mentioned in [Poking at Causation 1](http://howonlee.github.io/2016/01/21/Poking-20At-20Causation1.html).

A really fun thing is that using a threshhold instead of sampling from the ensemble sort of replicates the degree multiplicity problem Leskovec et al mentions in their original SKG work, I think.

This is BSD-licensed, made by NP Rougier, edited by Howon Lee. Thanks to Jeff Shrager for helping me poke at it.
