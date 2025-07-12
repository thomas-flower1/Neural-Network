# Creating a Neural Network from scratch using Python and Numpy

In this project I developed neurons, forwarding using the dot product, backpropogation and also wrote Relu and Softmax activation functions.
To calculate the loss I used the cross entropy loss function and passed the gradients through the network to train it.

## Resources
### Overview of Neural Networks
3Blue1Brown: [Introduction to Neural Networks](https://youtu.be/aircAruvnKk?si=M6Z-t2gqKkVAHlc8)
<br>
I also found the first half of [Andrej Karpathy's video](https://youtu.be/VMj-3S1tku0?si=PrqS_rUXRezc69Yy) on Neural Networks video helpful, especially the backpropogation exampes: 

### Backpropogation
This was the biggest challenge for me, the best videos on the topic I could find are:
<br>
Both 3Blue1Brown videos are good at getting a good overall understanding - [Video 1](https://www.youtube.com/watch?v=Ilg3gGewQ5U&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=3), [Video 2](https://www.youtube.com/watch?v=tIeHLnjs5U8&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=4)

The best video I think on the topic since it goes through and example with Softmax and Cross Entropy is: [Backpropogation](https://www.youtube.com/watch?v=VkHfRKewkWw)


### Some issues that I had: 
- What I was finding the derivative with respects to, just rembering to always derive the 'inputs' with respect to the loss function
- The output in the middle of one of my loss functions was a matrix of the input gradients - this wasn't mentioned much in the videos (if so i missed it), the solution is to just sum them or find the average and it returns a vector you can pass into the next layer
- Resetting the gradients for each new sample

### Credits
- Dataset used: [Kraggle](https://www.kaggle.com/datasets/jcprogjava/handwritten-digits-dataset-not-in-mnist)

### Usage
The network is trained with 80,000 samples. The data is loaded into the code for you to try!

