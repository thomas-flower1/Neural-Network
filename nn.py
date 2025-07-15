import numpy as np
from random import uniform, shuffle
from get_data import read_data

class Neuron:
    def __init__(self, n_inputs):
        self.w = np.array([uniform(-1, 1) for _ in range(n_inputs)])
        self.b = uniform(-1, 1)

        # forwards
        self.inputs = None # will either be a 2d matrix (for a batch) or will be a 1d array (for a single input)
        self.output = 0 # a single value that is the not product

        # backwards
        self.x_grad = None # gradient for the input
        self.w_grad = None # gradient ffor the weights
        self.b_grad = 0
        
    
    def forward_one(self, x):
        '''Takes a single input and fowards it through this neuron'''
        self.inputs = x
        self.output = np.dot(self.w, x) + self.b
        return self.output

    def backwards_one(self, gradient):
        # note that the gradient is just a single value at this point
        self.w_grad = self.inputs * gradient
        self.x_grad = self.w * gradient
        self.b_grad = gradient


class Layer:
    def __init__(self, layer_size, n_inputs):
        self.output = None # this will be a np array of all the outputs (dot product) of all the neurons of a single layer
        self.layer = [Neuron(n_inputs) for _ in range(layer_size)]
        self.inputs = None

        # backwards
        self.d_weights = []
        self.d_inputs = []
        self.d_b = []

    
    def forward(self, inputs):
        '''
        Takes an array of inputs and forwards them through the layer

        Returns an array containing all the outpus of the layer

        Args:
        inputs: numpy array of inputs
        '''
        self.inputs = inputs
        out = []
        for neuron in self.layer:
            out.append(neuron.forward_one(inputs))
        
        self.output = np.array(out)
        return self.output
    
    def backwards(self, gradients):  

        self.d_weights = []
        self.d_inputs = []
        self.d_b =[]

        for i, neuron in enumerate(self.layer):
          
            neuron.backwards_one(gradients[i])


            self.d_inputs.append(neuron.x_grad)
            self.d_weights.append(neuron.w_grad)
            self.d_b.append(neuron.b_grad)
        
        self.d_weights = np.array(self.d_weights)
        self.d_inputs = np.array(self.d_inputs)
        self.d_b = np.array(self.d_b)
        
    

    def update(self):
        learning_rate = 0.01
    
        for neuron in self.layer:
            neuron.w -= learning_rate * neuron.w_grad
            neuron.b -= learning_rate * neuron.b_grad
            
            # clear the gradients for the neuron
            neuron.b_grad = None
            neuron.w_grad = None
            neuron.b_grad = None

            # clear the layer gradients
        self.d_weights = []
        self.d_inputs = []
        self.d_b =[]

    def save(self, filename):
        '''Saves the weights and biases of the nn' by saving to a file'''

        with open(filename, 'a') as af:
            for neuron in self.layer:
                s = ''
                for num in neuron.w:
                    s = s + str(num) + ','
                af.write(s)
                af.write('\n')
    
    def load(self, filename):
        with open(filename) as rf:
            for i, line in enumerate(rf):
             

                str_arr = line.split(',')[:-1]
                weights = np.array([float(num) for num in str_arr])
            
                
                self.layer[i].w = weights.flatten()







class Relu:

    def __init__(self):
        self.output = None
        self.gradient = None
        self.inputs = None

    def forward_layer(self, dot_product_vector):
        '''Takes all the outputs of layer, passes through relu and outputs a vector'''
        # will return a vector
        self.inputs = dot_product_vector
        self.output = np.maximum(0, dot_product_vector)
        return self.output
    

    def backward_layer(self, gradients):
        relu_gradient = self.inputs > 0
        self.gradient = gradients * relu_gradient
        return self.gradient
        


class Softmax:
    
    def __init__(self):
        self.output = None # a vector holding all the outputs of a layer


    def forward(self, neuron_outputs):
        vector = []

        denominator = sum([np.exp(num) for num in neuron_outputs])
        for neuron in neuron_outputs:
            softmax = np.exp(neuron) / denominator
            vector.append(softmax)
        
        self.output = np.array(vector)
        return self.output
        

    # dont need a backwards function since handles in the loss function
    


        

class Loss:

    def __init__(self):
        self.loss = None
        self.gradient = None

    def forward_layer(self, outputs, targets):
        '''
        Example

        [0.5, 0.4, 0.1] = ouutput
        [0, 0, 1] = target (one hot encoded)

        This loss if for only one input into the network not a batch
        
        
        '''
        small_num = 1e-15
        # may have an error for when the loss is 0, fix later
        np.clip(outputs, small_num, 1 - small_num)
        self.loss = -np.sum(np.log(outputs) * targets)
        return self.loss


    

    def backwards_layer(self, predictions, targets):
        '''
        Backwards for all predictions and targets

        derivative is y_hat - y
        
        Return the gradient for the cross entropy loss and the softmax function

        



        '''
        self.gradient = predictions - targets
        return self.gradient

    


class Data:
    def __init__(self, value, data, target):
        self.value = value
        self.data = data
        self.target = target
    
    def __repr__(self):
        return f'{self.value}, {self.target}'





if __name__ == '__main__':

    # filenames = ['dataset1/zero_data.txt', 'dataset1/one_data.txt', 'dataset1/two_data.txt', 'dataset1/three_data.txt', 'dataset1/four_data.txt', 'dataset1/five_data.txt', 'dataset1/six_data.txt', 'dataset1/seven_data.txt', 'dataset1/eight_data.txt',
    #            'dataset1/nine_data.txt']


    # filenames = ['dataset2/zero.txt', 'dataset2/one.txt', 'dataset2/two.txt', 'dataset2/three.txt', 'dataset2/four.txt', 'dataset2/five.txt', 'dataset2/six.txt', 'dataset2/seven.txt', 'dataset2/eight.txt', 'dataset2/nine.txt']

    filenames = ['dataset2test/test0.txt', 'dataset2test/test1.txt', 'dataset2test/test2.txt', 'dataset2test/test3.txt', 'dataset2test/test4.txt', 'dataset2test/test5.txt', 'dataset2test/test6.txt', 'dataset2test/test7.txt', 'dataset2test/test8.txt', 'dataset2test/test9.txt']

    # loading inputs with their target
    inputs = []
    for i in range(len(filenames)):
        target = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        target[i] = 1

        matrix = read_data(filenames[i])
        for arr in matrix:
            data = Data(i, arr, target)
            inputs.append(data)

    input_size = 784 # size of how long a single training example is 
    shuffle(inputs)

    # TRAINING !!!

    layer1 = Layer(256, input_size)
    layer2 = Layer(10, 256)

    # activation functions
    relu = Relu()
    softmax = Softmax()

    loss = Loss()
       
    epoch = 10
    # for _ in range(epoch): # train on the same data 5 times (epoch)
    #     for input in inputs:
    #         data = input.data
    #         target = input.target

        
    #         # forward
    #         layer1.forward(data)
    #         relu.forward_layer(layer1.output)

    #         layer2.forward(relu.output)
    #         softmax.forward(layer2.output)


    #         # loss
    #         loss.forward_layer(softmax.output, target)
    #         # print("Loss", loss.loss)
            

    #         #backwards
    #         loss.backwards_layer(softmax.output, target)
    #         layer2.backwards(loss.gradient)

    #         relu.backward_layer(np.sum(layer2.d_inputs, axis=0)) # would be better to do the average
    #         layer1.backwards(relu.gradient)


    #         #update
    #         layer1.update()
    #         layer2.update()
    
    # Saving weights
    # savefile1 = 'layer1weights.csv'
    # savefile2 = 'layer2weights.csv'

    savefile1 = 'selfweights1.csv'
    savefile2 = 'selfweights2.csv'

    # layer1.save(savefile1)
    # layer2.save(savefile2)


    # loding data
    layer1.load(savefile1)
    layer2.load(savefile2)


    # lets check our neural network
    correct = 0
    number_of_iterations = len(inputs)

   
    for input in inputs:

        test_data = input
        data = test_data.data
        target = test_data.target

        # forward
        layer1.forward(data)
        relu.forward_layer(layer1.output)
        layer2.forward(relu.output)
        softmax.forward(layer2.output)
        
        # prediction
        predicted = np.argmax(softmax.output)
        actual = np.argmax(target)
        
        # print(f'Prediction: {predicted}')
        # print(f'Actual: {actual}')

        if actual == predicted:
            correct += 1

        
    print(f'Accuracy: {correct / number_of_iterations * 100}')




    



    
    

    




  

   


   









        
