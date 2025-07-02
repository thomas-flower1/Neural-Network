#include <iostream>
#include <vector>
#include <random>
#include "matrix_functions.h"
#include <numbers>

class Dense_Layer {
    private:
        std::vector<std::vector<double>> weights{}; // where each row is the weights for a single neuron
        std::vector<double> bias{}; // where each value is a bias for a neuron
        std::vector<std::vector<double>> output{};

    public:
        Dense_Layer(int n_input_neurons=0, int n_layer_neurons=0)
        : weights{generate_random_weights(n_input_neurons, n_layer_neurons)}, bias(n_layer_neurons, 0.0) {
    

        }
        
         

        double generate_number() {
            // will generate a number between -1 and 1;

            std::mt19937 mt{std::random_device{}()}; //  random device as the seed
            std::uniform_real_distribution<double> gaussian_dist{-1.0, 1.0};
            return gaussian_dist(mt);
        }

        std::vector<std::vector<double>> generate_random_weights(int rows, int cols) {
            // first create an empty matrix
            std::vector<std::vector<double>> w(rows, std::vector<double>(cols, 0.0));

            // then need to iterate over the whole thing
            for(int i{0}; i < rows; i++) {
                for(int j{0}; j < cols; j++) {
                    w[i][j] = generate_number();
                }
            }

           

            return w;
        }

        void forward(std::vector<std::vector<double>>& inputs) {
           

            std::vector<std::vector<double>> tmp{matrix_product(inputs, weights)};

        
            output = vector_matrix_addition(tmp, bias);

        }
        void print() {
            print_matrix(output);

        }

        std::vector<std::vector<double>> get_output() {
            return output;
        }
    };

class Relu{
    private:
        std::vector<std::vector<double>> output{};

        std::vector<double> relu_vector(const std::vector<double>& inputs) {
        
        // runs the relu function on a vector
        std::vector<double> outputs{};
        for(double input: inputs) {
            if(input > 0){
                outputs.push_back(input);
            } else {
                outputs.push_back(0);
            }

        }
        return outputs;

        
    }
    
    public:
        void forward(const std::vector<std::vector<double>>& matrix) {

            // given a matrix of inputs, apply the relu function and set it to the output

            std::vector<std::vector<double>> out{};
            for(auto row: matrix) {
                auto relu_row{relu_vector(row)};
                out.push_back(relu_row);
            }

            output = out;
        }

        auto get_output() {
            return output;
        }

        void print() {
            if(output.size() != 0) {
                print_matrix(output);
            }
           
        }
        

};

class Softmax{
    private:
        std::vector<std::vector<double>> output{};

        std::vector<double> softmax(const std::vector<double>& inputs) {


            // applies the softmax function on a set of inputs
            std::vector<double> exp{};

            for (auto in: inputs) {
                exp.push_back(std::pow(std::numbers::e, in));
            }


            // then we want to normalize our results
            double sum{0};
            for(auto e: exp) {
                sum += e;
            }


            // then divide each value
            std::vector<double> norm_values{};
            for(auto e: exp) {
                norm_values.push_back(e / sum);
            }

            return norm_values;

        }
    
        public:
            void forward(const std::vector<std::vector<double>>& matrix) {

                std::vector<std::vector<double>> out{};

                for(auto row: matrix) {
                    auto softmax_row{softmax(row)};
                    out.push_back(softmax_row);
                }

                output = out;

            }

            void print() {
                print_matrix(output);
            }


};



int main() {
    
    // making a single neuron
    std::vector<std::vector<double>> inputs{
        {1.0, 2.0, 3.0, 2.5},
        {2.0, 5.0, -1.0, 2.0},
        {-1.5, 2.7, 3.3, -0.8}
    };

    Dense_Layer layer{4, 4};
    layer.forward(inputs);
   
    std::cout << "The output of the dense layer with no activation function is: " << "\n";
    layer.print(); // printing the results
   
    // now we have an output from the dense layer (with no bias and random weights)
    // lets now pass it through the relu funcion
    Relu relu{};
    relu.forward(layer.get_output()); // makes it so either 0 or a positive number

    std::cout << "\n" << "The output with the reu activation function" << "\n";
    relu.print();

     // now lets forward the dense layer output
    Softmax softmax{};
    softmax.forward(layer.get_output());

    std::cout << "\n" << "Output with the softmax activation function" << "\n";
    softmax.print();
   

  
 

    

    

    

    return 0;
}