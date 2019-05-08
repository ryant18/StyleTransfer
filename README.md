first research paper: https://arxiv.org/abs/1508.06576
second resarch paper: https://arxiv.org/abs/1901.03915

Code for the gatys was taken from https://medium.com/tensorflow/neural-style-transfer-creating-art-with-deep-learning-using-tf-keras-and-eager-execution-7d541ac31398
it was modified to print out nicely formatted comparison images along with graphs of loss vs time.

Each image was used as a style and a content image for every other image (every single pair of images was computed). They were all run for 1000 training iterations
The problem is that loss does not nesecarily correspond to a realistic image
The loss graph for bluejay cardinal is very low, but the ouput image looks terrible. Compared to the loss of bluejay starry night, the ouput image looks much more realistic.
The loss is on a log graph, so the gap is larger than it seems. So loss doesnt always correspond to a better image which is the downfall of the network.

If you look at any of the images of orange forest, you can see that the network is looking at the overall image. So you get vertical streaks of brown lines throughout the image. This obviously isn't what we want. Ideally, the network would recgonize that the trees are a different part and only take the orange leaf pattern. This is what the image segmentation aims to do.

The second network with segmentation is much more customizable. I was only running the first bad batch of images for 1000 iterations to be consistent, but it looks like either learning rate is too low or im not running it for enough iterations. I'm currently running some more tests, but it much slower than the first method.

