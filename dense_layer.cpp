#include <iostream>
#include <vector>
#include <random>

class Dense_Layer {
    private:
        std::vector<std::vector<double>> weights{}; // where each row is the weights for a single neuron
        std::vector<std::vector<double>> bias{}; // where each value is a bias for a neuron

    public:
        Dense_Layer(int n_input_neurons=0, int n_layer_neurons=0)
            {

        }

        double generate_number() {
            // will generate a number between -1 and 1;

            std::mt19937 mt{std::random_device{}()}; //  random device as the seed
            std::uniform_real_distribution<double> gaussian_dist{-1.0, 1.0};
            return gaussian_dist(mt);
        }

        std::vector<std::vector<double>> generate_random_weights(int rows, int cols) {
            // first create an empty matrix
            std::vector<std::vector<double>> weights{rows, }
        }


};

int main() {
    Dense_Layer tmp{};
    tmp.generate_number();


    return 0;
}