#include <iostream>
#include <vector>
#include <random>
#include "matrix_functions.h"

class Dense_Layer {
    private:
        std::vector<std::vector<double>> weights{}; // where each row is the weights for a single neuron
        std::vector<double> bias; // where each value is a bias for a neuron
        std::vector<double> output{};

    public:
        Dense_Layer(int n_input_neurons=0, int n_layer_neurons=0)
        : weights{generate_random_weights(n_input_neurons, n_layer_neurons)}, bias(n_layer_neurons,0) {

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
            ;

        }

        







};

int main() {
    
    // making a single neuron
    std::vector<std::vector<double>> inputs{
        {1.0, 2.0, 3.0, 2.5},
        {2.0, 5.0, -1.0, 2.0},
        {-1.5, 2.7, 3.3, -0.8}
    };

    std::vector<std::vector<double>> weights{
        {0.2, 0.8, -0.5, 1.0},
        {0.5, -0.91, 0.26, -0.5},
        {-0.26, -0.27, 0.17, 0.87}

    };

    print_matrix(weights);

    

    

    

    return 0;
}